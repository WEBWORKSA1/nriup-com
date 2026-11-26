# NRIup.com — Phase-wise Build Prompts

Use these prompts in order to rebuild, audit or extend **nriUP — Uttar Pradesh, from anywhere**. Each phase ends with a check; don't move on until it passes.

---

## Phase 0 — Guardrails (paste first in every session)
> You are building **NRIup.com (brand: nriUP)**, a static, Jekyll-compatible website hosted free on GitHub Pages (repo `WEBWORKSA1/nriup-com`, branch `main`, root). It is the independent hub for NRIs, OCIs, Gulf workers and Girmitiya descendants with property, family, roots or plans in Uttar Pradesh. Rules:
> - Every page loads in `<head>`: `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>` plus `<meta name="google-adsense-account" content="ca-pub-6620975821265271">`. Auto ads only; never fake ad boxes; never ask users to click ads.
> - A top bar on every page reads “Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership” and the whole sentence links to `https://web.works/contact`. The text “web.works” is never visible.
> - All forms post to one private inbox through FormSubmit's AJAX endpoint. The inbox address is rebuilt at runtime from an XOR-obfuscated, reversed char-code array in `main.js`; it never appears in HTML, text or source as a literal. Every form has a honeypot (`_honey`) and a consent checkbox.
> - Not a government site: never use state emblems or imply affiliation with the Government of UP, its NRI Department or the UP NRI Card. Trademark & copyright disclosure in the footer and on `/trademark.html`.
> - Information only, no legal/tax advice. Every statistic and rule must cite a primary or reputable source and be verified. No fabricated testimonials, ratings or user counts.
> - Vanilla HTML/CSS/JS. Mobile-first, accessible, light/dark theme. No trackers beyond AdSense.

## Phase 1 — Positioning & research
> Research at least 38 comparable sites (state NRI portals, UP government portals, NRI fintech and remittance, NRI legal/property, elder care, diaspora media/NGOs, temple and pilgrimage portals, donation platforms, contest platforms). Open each one and record what it actually does and what to borrow in `RESEARCH.md`. Verify the core numbers: UP's emigration clearances (Rajya Sabha via data.gov.in), the share of girmitiyas from UP (Brij V. Lal, ANU Press), India's remittances (RBI), the Income-tax Act 2025 residency and TDS rules, UP stamp duty, Noida International Airport dates.
> **Check:** positioning sentence fits in one line: “Uttar Pradesh, handled from anywhere.”

## Phase 2 — Foundation
> Create `_config.yml` (url https://nriup.com; exclude README, BUILD-PROMPTS, RESEARCH, scripts), `CNAME` (nriup.com), `ads.txt` (`google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0`), `robots.txt`, Liquid `sitemap.xml` over `site.html_pages` (skip `sitemap: false`), `site.webmanifest`, SVG favicon and OG image, `_data/build.yml`. Build `_layouts/default.html` (SEO meta, canonical, OG, Organization + WebSite JSON-LD, optional `page.schema`, AdSense, theme pre-paint script, top bar, sticky header with nav: Property, Money, Roots, Gulf & jobs, Family, Visit, Invest, Tools, Guides + “Free case review” CTA; footer with newsletter, four link columns and disclosure; mobile sticky CTA bar; once-per-session nudge; cookie notice). Build `_layouts/guide.html` (hero with review date and read time, prose, sources list from front matter, CTA band keyed by `cta_service`, Article JSON-LD) and `_includes/quick-form.html` (service-tagged quick lead form).
> **Check:** every page shows top bar, AdSense tag and footer disclosure.

## Phase 3 — Design system
> `assets/css/style.css`: ink #0d1330, saffron #ff8a1f, gold #f5c044, Ganga teal #0fa38c, cream #fffaf2; Fraunces (display) + Plus Jakarta Sans (body). Components: buttons, cards, stats, hero with arch motif and quick-need form, page hero, hub two-column layout with sticky aside, split layout, form card, tiles, multi-step bar, summary, tool panel + dark result panel, tables, badges, callouts, prose, FAQ details, news cards with filters, video facades, district grid, tiers, fund bars, timeline, checklist, footer, nudge, cookie. Content must be visible without JS (no hidden-until-scrolled reveals).
> **Check:** 390px, 768px, 1366px, light and dark.

## Phase 4 — Engine (`assets/js/main.js`)
> Theme, burger, active nav, year, cookie, nudge (45s or 62% scroll; not on get-help/thank-you/contact), UTM + landing + referrer capture, `data-mail` links, 75 districts in 18 divisions with region labels and Girmit-era origin flags (Basti, Gonda, Azamgarh, Sultanpur, Ayodhya, Bahraich) populating every `select[data-districts]`, district finder, generic FormSubmit AJAX handler (service-key → label mapping, subject with service + district, `_template: table`, `_autoresponse`, attribution, thank-you redirect, activation-pending message, mailto fallback), JSON loader that tries `raw.githubusercontent.com/WEBWORKSA1/nriup-com/main/data/` then `/data/`.
> **Check:** `node --check`; headless test shows the endpoint decodes correctly and the honeypot blocks.

## Phase 5 — Lead generation (highest priority)
> `/get-help.html`: 4-step funnel — (1) 12 service tiles (property care, dispute, mutation, sell + TDS certificate, buy, NRI tax, roots, parents' care, business, overseas job help, visit, other) that auto-advance; (2) district, locality, urgency tiles, value band, details; (3) name, email, WhatsApp, country, language, best time; (4) live summary, hidden lead score (service weight + urgency + phone + budget → HOT/WARM/NURTURE), consent, optional partner-share opt-in. Prefill from `?service=&district=`. Feed it from the hero quick-need form, every hub's sticky quick form, guide CTA bands, tool results (e.g. “Get a CA to apply for my certificate”), the nudge and the mobile bar.
> **Check:** prefill jumps to step 2; payload contains service label, district, lead score, attribution; partners only see leads with opt-in.

## Phase 6 — Tools
> Property-sale TDS (12.5% LTCG + 10%/15% surcharge + 4% cess on full price vs estimated tax on gain → “cash locked”; STCG at 30% assumption); UP stamp duty (7% man, 6% woman ≤₹1 crore, 6.5% joint woman+man ≤₹1 crore, 1% registration, ₹5,000 + ₹1,000 family gift deed, on the higher of deal and circle value); transfer true cost (live mid-market vs up to 3 quotes); residential status (182; 60+365; 182 for emigrating citizens and low-income visitors; 120 for >₹15 lakh Indian income → RNOR; deemed resident; RNOR via 9-of-10 or ≤729 days); NRE/NRO/FCNR picker; seven persistent, printable checklists with an “ask for help” form.
> **Check:** ₹80L/₹50L/60 months → TDS ₹11,44,000, tax ₹3,90,000, locked ₹7,54,000; ₹60L man → ₹4,80,000; woman → ₹4,20,000.

## Phase 7 — Hubs & guides (AdSense-grade content)
> Hubs: property, money, roots, gulf, family, visit, invest, districts, news, videos — each 500–900 words of original, sourced text plus a sticky quick form. Guides (600–1,000 words, dated, sourced): buying property as an NRI; khatauni, Bhulekh and mutation; selling and TDS in 2026 (section 393, Form 128, PAN-based Form 141 from 1 Oct 2026); power of attorney from abroad; residential status under the 2025 Act; sending money (true cost); Girmitiya roots tracing; safe migration from UP; Noida International Airport. Add about (with “our numbers” source table), contact, privacy (Google advertising cookie language, opt-outs, FormSubmit, GDPR/UK GDPR/PIPEDA/Law 25/DPDP/CCPA), cookies, terms, disclaimer, editorial policy (incl. AI-assisted drafting with human fact-checks), trademark, 404, thank-you.
> **Check:** every number re-computed in code; every rule traced to its source.

## Phase 8 — Monetisation & community
> `/support.html`: tiers Ek Chai $5, Supporter $10/mo, Patron $25/mo, Founding sponsor $250+; use-of-funds bars (operations 35%, hiring 25%, contests & prizes 20%, promotion 20%); pledge form that emails a secure payment link (no card fields); “not tax-deductible”. `/contests.html`: Mera UP Season 1 — Roots Story, Photo of UP, 60-Second Film, Pravasi Hero; free entry, 18+, skill-judged (40/30/30), countdown, sponsor-funded prize pool target, full rules. `/careers.html`: six roles + application form + **expert network** application (advocates, CAs, surveyors, property managers, elder care, travel). `/advertise.html`: tool sponsorship, sponsored guide, newsletter, contest track, pay-per-lead partner network, domain/website enquiry card → web.works/contact; ad standards; media-kit form.
> **Check:** every paid placement labelled; no prohibited categories.

## Phase 9 — Automation
> `scripts/refresh.py` (stdlib only) + `scripts/sources.json`: daily INR mid-market rates for 20 diaspora currencies (open.er-api.com, fallback Frankfurter/ECB), Google News RSS headlines across 7 topics (title + publisher + link only), YouTube channel RSS and topic searches (IDs + titles only, click-to-load nocookie embeds), build date. Each part fails independently and keeps previous data. `.github/workflows/auto-refresh.yml`: daily 01:23 UTC + manual + on script changes; commit `data/` and `_data/` if changed; request a Pages rebuild.
> **Check:** run the workflow manually once; `data/*.json` populate; home ticker, news and videos render.

## Phase 10 — QA
> Build locally (Jekyll or an emulator), then: internal links resolve; AdSense + top bar on every page; no inbox address anywhere in source or output; “web.works” never visible; unique titles; descriptions ≤ 200 chars; no duplicate IDs; every `js-form` has a honeypot; headless runtime tests for every tool and the funnel; screenshots at 1366px and 390px.

## Phase 11 — Deploy
> Push to `WEBWORKSA1/nriup-com` on `main`. Settings → Pages → Deploy from a branch → `main` / root. Custom domain `nriup.com`, Enforce HTTPS. DNS: A @ → 185.199.108.153 / .109.153 / .110.153 / .111.153; CNAME www → webworksa1.github.io. Submit one form and click FormSubmit's activation email.

## Phase 12 — Launch & growth
> Search Console + sitemap; AdSense application with Google's certified CMP enabled; recruit 3–5 vetted partners in the five highest-demand districts first (Gautam Buddha Nagar, Lucknow, Varanasi, Prayagraj, Azamgarh/Ghazipur belt); 30–60s Shorts per guide linking to tools; WhatsApp communities for Gulf workers; outreach to Girmitiya associations in Fiji, Mauritius, Trinidad, Guyana and Suriname. Expansion: one landing page per district (75 pages, templated from the district data), Hindi versions of top guides, a paid “UP Property Watch” subscription (quarterly site visits + khatauni change alerts), a partner dashboard, and an embeddable stamp-duty widget for backlinks.
