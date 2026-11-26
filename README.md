# NRIup.com — nriUP: Uttar Pradesh, from anywhere

Independent hub for NRIs, OCIs, Gulf workers and Girmitiya descendants with property, family, roots or plans in Uttar Pradesh. Static Jekyll site, hosted free on GitHub Pages (`main` branch, root), monetised with Google AdSense, lead generation, sponsorships and supporter pledges.

## What's inside
| Area | Files |
|---|---|
| Layouts & shell | `_layouts/default.html` (SEO, AdSense, contact top bar, nav, footer, disclosure, cookie, nudge), `_layouts/guide.html`, `_includes/quick-form.html` |
| Design system | `assets/css/style.css` (light/dark, mobile-first) |
| Engine | `assets/js/main.js` — forms → private inbox via FormSubmit (address assembled at runtime, never in HTML), 4-step lead funnel with lead scoring, 6 tools, 75-district data, live rates/news/videos, IST clock |
| Lead generation | `get-help.html` (4-step funnel), quick forms on every hub, `thank-you.html` |
| Hubs | `property`, `money`, `roots`, `gulf`, `family`, `visit`, `invest`, `districts`, `news`, `videos` |
| Tools | `tools/` — property-sale TDS, UP stamp duty, transfer true cost, residential status, NRE/NRO/FCNR picker, document checklists |
| Guides | `guides/` — 9 sourced guides |
| Monetisation & community | `support`, `contests`, `careers` (incl. expert network), `advertise` |
| Legal | `about`, `contact`, `privacy`, `cookies`, `terms`, `disclaimer`, `editorial-policy`, `trademark`, `404` |
| Automation | `scripts/refresh.py` + `scripts/sources.json`, run daily by `.github/workflows/auto-refresh.yml` (backup copy in `scripts/auto-refresh.yml`) |
| Docs | `BUILD-PROMPTS.md` (phase-wise build prompts), `RESEARCH.md` (41 sites reviewed, idea rationale, revenue model) |

## Publish (one-time)
1. **Settings → Pages** → Source: *Deploy from a branch* → Branch: `main` / `/ (root)` → Save.
2. Custom domain `nriup.com` (already in `CNAME`) → tick **Enforce HTTPS** once the certificate is issued.
3. DNS at the registrar: four `A` records for `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; `CNAME` for `www` → `webworksa1.github.io`.
4. **Actions** tab → *Auto-refresh site data* → *Run workflow* once to fill `data/*.json`.

## After launch
- **FormSubmit:** submit any form once; click the one-time activation link FormSubmit emails to the inbox.
- **AdSense:** add the site in AdSense, keep `ads.txt` as is, and turn on Google's certified consent message (Privacy & messaging) for EEA/UK/Swiss visitors.
- **Search Console:** verify `nriup.com` and submit `https://nriup.com/sitemap.xml`.

## Editing
- News queries, video searches, channels and currencies: `scripts/sources.json`.
- Districts and checklists: data arrays at the top of the relevant sections in `assets/js/main.js`.
- New guide: copy any file in `guides/`, keep the front matter (`layout: guide`, `reviewed`, `sources`, `cta_service`), and link it from `guides/index.html`.
