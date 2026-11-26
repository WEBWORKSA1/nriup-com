#!/usr/bin/env python3
"""nriUP daily refresh: INR rates, news headlines and YouTube videos -> data/*.json.

Standard library only. Each part fails independently and keeps the previous data,
so one broken source never empties the site. Edit scripts/sources.json to change
currencies, news queries, channels or video searches.
"""
import datetime as dt
import json
import pathlib
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "scripts" / "sources.json").read_text())
UA = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "CONSENT=YES+1",
}


def get(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def save(name, obj):
    (ROOT / "data" / name).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def iso(s):
    try:
        return parsedate_to_datetime(s).astimezone(dt.timezone.utc).replace(microsecond=0).isoformat()
    except Exception:
        return None


def rates():
    curs = CFG["currencies"]
    out, src = {}, ""
    try:
        j = json.loads(get("https://open.er-api.com/v6/latest/INR"))
        if j.get("result") != "success":
            raise ValueError(j.get("result"))
        out = {c: round(1 / j["rates"][c], 4) for c in curs if j["rates"].get(c)}
        src = "open.er-api.com"
    except Exception as e:
        print("rates: primary failed:", e)
        j = json.loads(get("https://api.frankfurter.app/latest?from=INR"))
        out = {c: round(1 / j["rates"][c], 4) for c in curs if j["rates"].get(c)}
        src = "frankfurter.app (ECB)"
    if len(out) < 5:
        raise ValueError("too few rates")
    save("rates.json", {"updated": now(), "source": src, "inr_per": out})
    print("rates:", len(out), "currencies from", src)


def news():
    items, seen = [], set()
    for topic, q in CFG["news"]:
        url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
            {"q": q + " when:7d", "hl": "en-IN", "gl": "IN", "ceid": "IN:en"})
        try:
            root = ET.fromstring(get(url))
        except Exception as e:
            print("news:", topic, "failed:", e)
            continue
        n = 0
        for it in root.iter("item"):
            title = (it.findtext("title") or "").strip()
            link = (it.findtext("link") or "").strip()
            src = (it.findtext("source") or "").strip()
            if src and title.endswith(" - " + src):
                title = title[: -len(src) - 3].strip()
            key = re.sub(r"\W+", "", title.lower())[:80]
            if not title or not link.startswith("http") or key in seen:
                continue
            seen.add(key)
            items.append({"t": title[:220], "u": link, "s": src[:80], "d": iso(it.findtext("pubDate") or ""), "topic": topic})
            n += 1
            if n >= 14:
                break
    if not items:
        raise ValueError("no news items")
    items.sort(key=lambda i: i["d"] or "", reverse=True)
    save("news.json", {"updated": now(), "items": items[:100]})
    print("news:", len(items), "items")


NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}


def channel_id(handle):
    if handle.startswith("UC"):
        return handle
    page = get("https://www.youtube.com/" + handle).decode("utf-8", "ignore")
    m = re.search(r'"(?:externalId|channelId)":"(UC[\w-]{22})"', page) or re.search(r"channel_id=(UC[\w-]{22})", page)
    return m.group(1) if m else None


def channel_videos(handle, topic, limit=6):
    cid = channel_id(handle)
    if not cid:
        raise ValueError("channel id not found")
    root = ET.fromstring(get("https://www.youtube.com/feeds/videos.xml?channel_id=" + cid))
    out = []
    for e in root.findall("a:entry", NS)[:limit]:
        vid = e.findtext("yt:videoId", namespaces=NS)
        out.append({"id": vid, "t": (e.findtext("a:title", namespaces=NS) or "")[:160],
                    "c": e.findtext("a:author/a:name", namespaces=NS) or "",
                    "d": e.findtext("a:published", namespaces=NS), "topic": topic})
    return out


def search_videos(q, topic, limit=6):
    url = "https://www.youtube.com/results?" + urllib.parse.urlencode({"search_query": q, "hl": "en", "gl": "US"})
    page = get(url).decode("utf-8", "ignore")
    out = []
    for m in re.finditer(r'"videoRenderer":\{"videoId":"([\w-]{11})"', page):
        chunk = page[m.end(): m.end() + 6000]
        t = re.search(r'"title":\{"runs":\[\{"text":"((?:[^"\\]|\\.)*)"', chunk)
        o = re.search(r'"ownerText":\{"runs":\[\{"text":"((?:[^"\\]|\\.)*)"', chunk)
        if not t:
            continue
        try:
            title = json.loads('"' + t.group(1) + '"')
            owner = json.loads('"' + o.group(1) + '"') if o else ""
        except Exception:
            continue
        out.append({"id": m.group(1), "t": title[:160], "c": owner[:80], "d": None, "topic": topic})
        if len(out) >= limit:
            break
    return out


def videos():
    items, seen = [], set()

    def add(lst):
        for v in lst:
            if v.get("id") and re.fullmatch(r"[\w-]{11}", v["id"]) and v["id"] not in seen:
                seen.add(v["id"])
                items.append(v)

    for handle, topic in CFG.get("youtube_channels", []):
        try:
            add(channel_videos(handle, topic))
        except Exception as e:
            print("videos: channel", handle, "failed:", e)
    for topic, q in CFG.get("youtube_searches", []):
        try:
            add(search_videos(q, topic))
        except Exception as e:
            print("videos: search", q, "failed:", e)
    if not items:
        raise ValueError("no videos")
    save("videos.json", {"updated": now(), "items": items[:72]})
    print("videos:", len(items), "items")


def build_date():
    (ROOT / "_data" / "build.yml").write_text('updated: "%s"\n' % dt.date.today().isoformat())


if __name__ == "__main__":
    for job in (rates, news, videos):
        try:
            job()
        except Exception as e:
            print(job.__name__, "kept previous data:", e)
    build_date()
