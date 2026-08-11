---
title: "data.gov — the US Federal Catalogue"
date: 2026-08-11
publishers: ["US General Services Administration"]
regions: ["North America"]
place: "United States"
places: ["United States"]
domains: ["Governance", "Geospatial"]
licenses: ["US Public Domain", "CC0 1.0"]

source: "https://catalog.data.gov/"
version: "Catalogue as at 11 August 2026 — ~548,745 dataset URLs; API absent, 30 pages sampled by scraping"
snapshot: 2026-08-11
temporal: "Varies by agency"
updated: "Unassessable — no catalogue-level modification data is exposed"
cadence: "Not declared, and not measurable"
formats: ["Varies by agency; not enumerable without an API"]
size: "~548,745 dataset URLs across 110 sitemap shards"
access: "Browsable and ungated; no API, no bulk inventory"

verdict: "The largest open data catalogue on earth, and the only way left to read it is one page every ten seconds."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 4
  documentation: 4
  accessibility: 4
  licensing: 8
  interoperability: 4

strengths:
  - "**~548,745 datasets** — by a wide margin the largest catalogue we have measured, aggregating federal, state and local publishers into one index."
  - "**80% of sampled datasets declare an explicit open licence** — 18 of 30 CC0, 6 the US Government public domain label. Against [New York's 2.6%](/evaluations/nyc-open-data/), that is a different standard of practice."
  - "Every dataset page embeds schema.org JSON-LD with `dateModified`, `license`, `publisher`, `keywords` and `distribution`, so a single record is machine-readable even without an API."
weaknesses:
  - "**The CKAN API is gone.** Every documented endpoint — `/api/3/action/package_search`, `package_list`, `status_show`, the v2 search API — returns 404."
  - "**`data.json` returns 404**, on both `catalog.data.gov` and `data.gov`. NASA's agency inventory at the same standard path serves 89.8 MB. The federal mechanism works; the national aggregator has stopped exposing one."
  - "`/developers/` is a 404, `robots.txt` still carries `# TODO: add disallow routes`, and `Crawl-Delay: 10` means reading the catalogue by scraping would take 63 days."

bestfor:
  - "Finding out whether a US public dataset exists, one search at a time"
  - "Single-dataset lookups, where the embedded JSON-LD is genuinely useful"
avoidfor:
  - "Any harvesting, mirroring or systematic assessment — there is no supported route"
  - "Pipelines built on the CKAN API or on data.json; both are gone"
  - "Judging catalogue freshness, which cannot currently be measured from outside"
---

## What it is

The United States federal open data catalogue: roughly **548,745 dataset URLs**, counted from 110
sitemap shards of 5,000 entries plus a partial final shard. Federal agencies, states, counties and
cities, indexed in one place. It is the largest catalogue on this site by an order of magnitude — for
comparison, [Italy's national catalogue](/evaluations/dati-gov-it/) holds 65,828.

**A note on evidence, because it is unusually important here.** Most evaluations on this site rest on
a few thousand API calls. This one could not. The catalogue exposes no API, so the structural
findings below were established by probing a dozen documented endpoints, and the freshness and
licensing figures come from **30 dataset pages scraped at eleven-second intervals**, honouring the
`Crawl-Delay: 10` the site requests. Thirty is a small sample and we treat it as indicative rather
than measured. That we could not do better is the finding.

## How it holds up

**The scale is real and the licensing is good.** Of the 30 pages sampled, 24 carry an explicit open
licence — 18 CC0, 6 the `usa.gov` public domain label — and 6 declare none. **80% licensed** is a
strong result, and it throws the [NYC portal](/evaluations/nyc-open-data/), where 97.4% of assets
state nothing, into unflattering relief. Federal practice on rights is clearly better than municipal
practice, at least here.

The JSON-LD is a genuine strength too. Every page we fetched embedded schema.org structured data with
`name`, `description`, `keywords`, `publisher`, `license`, `datePublished`, `dateModified` and
`distribution`. A machine reading a single dataset page gets clean, standards-based metadata.

**And then there is no way to read more than one page at a time.**

Every documented programmatic route is gone:

| Endpoint | Result |
|---|---|
| `/api/3/action/package_search` | 404 |
| `/api/3/action/package_list` | 404 |
| `/api/3/action/status_show` | 404 |
| `/api/2/search/dataset` | 404 |
| `catalog.data.gov/data.json` | 404 |
| `data.gov/data.json` | 404 |
| `/developers/` | 404 |

The CKAN API is the interface a decade of civic technology was built against. `data.json` is the
Project Open Data inventory format that the federal open data policy established, and it is the
mechanism by which agency catalogues are harvested in the first place. Both now return 404 at the
national catalogue.

The mechanism itself has not been abandoned government-wide. We checked NASA's inventory at the
standard path and it returns **89.8 MB of JSON**. Agencies are still publishing machine-readable
inventories to the federal standard. What has stopped is the aggregator exposing one of its own — so
the catalogue can ingest at scale and cannot be read at scale.

The supporting details suggest a rebuild that has not finished. `/developers/` is a 404 rather than a
redirect. `robots.txt` is in production carrying the comment `# TODO: add disallow routes` and a note
that the sitemap URL "should get replaced by proxy .profile". `Crawl-Delay: 10` is the only stated
access policy, and at that rate reading all 548,745 datasets would take **63 days of continuous
requests**.

**Freshness we can only estimate, and it is not good.** Across the 30 sampled pages the median
`dateModified` was **1,045 days — 2.9 years**. 43.3% were over four years old; exactly one of thirty
had been modified within the past month. We first tried to measure this properly from sitemap
`lastmod` and discarded the attempt: eleven of thirteen shards carried a single identical date for
all 5,000 entries, so `lastmod` reflects sitemap generation, not dataset modification. It is not a
usable signal and we do not report one.

## Working with it

If you have a pipeline built on the CKAN API or on `data.json`, it is broken and there is no
documented replacement. Go to the publishing agency's own inventory instead — NASA, NOAA, Census and
others still serve `data.json` at the standard path, and that is now the only supported way to
harvest federal data at scale.

For single lookups, parse the JSON-LD embedded in the dataset page. It is clean and it is there.

Honour the crawl delay. The catalogue asks for ten seconds and has no other way to protect itself.

## The call

**Grade C+.** The holdings are enormous and the rights position is genuinely good — better than most
of the municipal portals on this site. The substance deserves an A.

The delivery does not. A catalogue's entire function is to be the machine-readable index to
everything else, and this one currently cannot be queried, harvested or mirrored by any documented
means. Restoring `data.json` alone — one file, from data the catalogue already holds — would move
this several grades in an afternoon and reconnect every federal harvesting pipeline that is presently
broken.

We will re-evaluate when the API returns. Given the state of `robots.txt`, we suspect this is a
rebuild in progress rather than a policy, and we would rather record that it was measured during one
than imply it is permanent.
