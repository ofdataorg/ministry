---
title: "Comune di Bologna Open Data"
date: 2026-07-30
publishers: ["Comune di Bologna"]
regions: ["Europe"]
domains: ["Governance", "Geospatial", "Mobility"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/"
temporal: "Varies by dataset; several statistical series run back decades"
updated: "Continuously for the automated feeds; much of the rest has not moved in years"
cadence: "Not stated on a single dataset in the catalogue"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX", "SHP", "GPX"]
size: "702 datasets, 43,031,850 records"
access: "Open API and bulk download, no registration"

verdict: "One of the cleanest municipal licences in Europe wrapped around a catalogue where the machines keep their promises and the humans do not."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 4
  documentation: 5
  accessibility: 9
  licensing: 9
  interoperability: 7

strengths:
  - "692 of 702 datasets carry a single unmodified CC BY 4.0 licence — 98.6% of the catalogue under one set of terms a reader can check in a minute."
  - "No registration, no click-through, no rate-limit theatre. A full CSV export of a 1.5-million-row dataset returned in a couple of seconds."
  - "Seven export formats including **Parquet** and GeoJSON, plus a DCAT/RDF export of the whole catalogue. Municipal portals almost never ship columnar formats."
weaknesses:
  - "**Not one of the 702 datasets states an update frequency.** The field exists in the platform and is empty across the entire catalogue."
  - "31.8% of the catalogue has not been touched in over four years; the median dataset was last processed 468 days ago."
  - "27.7% of fields carry a description, and 43% of datasets document no field at all. The English metadata is a fiction — 699 of 702 English titles are the Italian string copied over."

bestfor:
  - "Mobility, territory and sensor data for Bologna, where the feeds are genuinely live"
  - "Geospatial work — 300 datasets carry geometry and export as GeoJSON or SHP"
  - "Anyone who needs a municipal licence that will survive a legal review"
avoidfor:
  - "Assuming a dataset's presence in the catalogue means anyone still maintains it"
  - "Administrative and governance series, where nearly two thirds are over two years stale"
  - "Non-Italian-speaking pipelines that trust the English metadata fields"
---

## What it is

The open data catalogue of the City of Bologna: 702 datasets and just over 43 million records,
running on Opendatasoft, covering territory, local government, transport, population, culture,
environment and a growing estate of live municipal sensors. All figures here were measured against
the catalogue API on 30 July 2026.

A note before anything else, because it cost us twenty minutes. The address the city advertises for
its data, `dati.comune.bologna.it/dati`, does not serve a catalogue. It serves the full text of the
Creative Commons Attribution 4.0 licence and a cookie banner, with no search, no dataset list, and
no link to the actual portal. The data lives at `opendata.comune.bologna.it`. A municipality whose
`/dati` URL returns a licence agreement instead of any data has mis-signposted the front door of its
own building.

## How it holds up

**The licensing is close to exemplary and deserves to be said first.** 692 of 702 datasets — 98.6% —
carry plain, unmodified CC BY 4.0. One licence, standard, no user-class distinction, no
research-versus-commercial split, no registration. The residue is small and mostly harmless: four
CC BY 3.0 IT, two CC BY 1.0, two Open Database Licence, one CC0. Exactly one dataset is CC BY-NC
3.0 IT, and that single non-commercial record is the only genuine trap in the whole catalogue — find
it before you build a product on a bulk download, because it will attach to whatever it touches.

This is what we have been asking for in [The Licence Is the Dataset](/analyses/the-licence-is-the-dataset/):
one licence, unmodified, for everyone. Bologna has done it. Most national portals have not.

**Accessibility is equally strong.** There is no gate of any kind. The Explore API answers, the bulk
exports work, and the URLs are guessable. Seven formats ship, including Parquet — which no other
municipal portal in this catalogue offers — and the whole catalogue exports as DCAT/RDF. For a city
of 400,000 people this is a serious piece of infrastructure.

**And then there is the clock.** This is where the evaluation turns, and the numbers are not
ambiguous:

| Last processed | Datasets | Share |
|---|---:|---:|
| Under 1 month | 183 | 26.1% |
| 1–6 months | 77 | 11.0% |
| 6–12 months | 22 | 3.1% |
| 1–2 years | 150 | 21.4% |
| 2–4 years | 47 | 6.7% |
| **Over 4 years** | **223** | **31.8%** |

The median dataset was last processed 468 days ago. 38.5% of the catalogue is more than two years
stale. Nearly a third has not moved in over four years.

That distribution is bimodal, and the split is the most interesting thing on this portal. Break the
staleness down by theme and the pattern is unmistakable:

| Theme | Stale over 2 years |
|---|---:|
| Governo e settore pubblico | 62.9% |
| Regioni e città | 46.7% |
| Istruzione, cultura e sport | 43.1% |
| Economia e finanze | 36.4% |
| Ambiente | 20.0% |
| Popolazione e società | 13.8% |
| Trasporti | 12.2% |
| Scienza e tecnologia | 5.6% |

**The automated feeds are alive and the human-maintained ones are dead.** Transport sensors, wifi
counters and air quality stations — the things that update because a machine pushes them — are
almost all current. Governance and administrative publishing, the things that update because a
person remembers to, has rotted at 62.9%. Nobody decided this. It is simply what happens when
publication depends on individual diligence and no process enforces it.

**Not one dataset states an update frequency.** Zero out of 702. The platform has the field; the
city has left it empty across the entire catalogue. This is the exact failure we set out in
[Fresh Is a Claim, Not a Property](/analyses/fresh-is-a-claim-not-a-property/): every dataset shows
a modification date, none states an intended cadence, and a reader has no way to distinguish a
series that is published annually and is not due yet from one that was abandoned in 2021. Both look
identical. Both are, as far as the metadata is concerned, fine.

**Documentation is thin below the surface.** Dataset-level descriptions are mostly present and
reasonable — only 14.2% run under 80 characters. Go one level down and it collapses: 3,489 of 12,591
fields carry a description, 27.7%, and 43% of datasets document no field whatsoever. On a sensor
feed with a column called `detectedobjects`, that is the difference between data and a guess.

The English metadata should be removed or finished. 699 of 702 English titles are byte-identical to
the Italian. Three datasets — 0.4% — are genuinely translated. The fields are populated, so an
automated consumer sees a bilingual catalogue and gets Italian. Serving Bologna's own public in
Italian is entirely legitimate; advertising an English layer that does not exist is not.

## Working with it

Go to `opendata.comune.bologna.it`, not the `/dati` URL. Use the Explore v2.1 API rather than
scraping the interface.

**Take Parquet or GeoJSON if you can.** The CSV export is the one genuinely user-hostile default on
the platform: semicolon-delimited, UTF-8 with a byte-order mark, CRLF line endings. Read it with
standard settings and you get a single column, and the BOM turns your first field name into
`﻿createdat`. Pass `?delimiter=,` and decode as `utf-8-sig` and it behaves — but the default
should not require knowing that.

Check the modification date of every dataset individually and treat the catalogue's overall activity
as telling you nothing about any specific holding. If you need a governance or administrative
series, verify it is current before building on it; the base rate says it is probably not.

One more for machine consumers: the Italian national metadata profile, DCAT-AP_IT, is populated on
exactly one dataset out of 702, and only with `publisher_id`. The European DCAT export at catalogue
level is real and substantial. The national profile is not filled in.

## The call

**Grade B.** The parts Bologna decided once and automated — licensing, access, formats — are done
better than most national portals manage, and the live sensor estate is genuinely impressive for a
city this size. The parts that depend on somebody remembering have decayed exactly as far as you
would predict, and the catalogue does not admit it anywhere a user would look.

The fix is not more data. It is one metadata field. Populate `update_frequency` on all 702 datasets
and mark the dormant ones dormant, and this portal tells the truth about itself for the first time —
and moves up a grade for the cost of an afternoon.
