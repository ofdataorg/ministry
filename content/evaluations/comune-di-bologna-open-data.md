---
title: "Comune di Bologna Open Data"
date: 2026-07-30
publishers: ["Comune di Bologna"]
regions: ["Europe"]
domains: ["Governance", "Geospatial", "Mobility"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/"
temporal: "Varies by dataset; several statistical series run back decades"
updated: "Continuously for the automated feeds; half the catalogue is declared one-off"
cadence: "Declared on all 702 via dcat:accrualPeriodicity; 82.4% of testable promises honoured"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX", "SHP", "GPX"]
size: "702 datasets, 43,031,850 records"
access: "Open API and bulk download, no registration"

verdict: "One of the cleanest municipal licences in Europe, and a catalogue that tells the machines exactly what it intends to do while telling the reader almost nothing."
reviewer: "Ministry desk"

corrections:
  - date: 2026-07-30
    text: "This evaluation originally scored timeliness **4** and stated that no dataset declared an update frequency. That was wrong. We checked only the portal's native `update_frequency` field and missed `dcat:accrualPeriodicity`, which is populated on all 702 datasets. Timeliness re-scored to **8** and the section rewritten around declared-versus-observed cadence. Thanks to the reader who pointed it out."

scores:
  completeness: 7
  timeliness: 8
  documentation: 5
  accessibility: 9
  licensing: 9
  interoperability: 7

strengths:
  - "692 of 702 datasets carry a single unmodified CC BY 4.0 licence — 98.6% of the catalogue under one set of terms a reader can check in a minute."
  - "No registration, no click-through, no rate-limit theatre. A full CSV export of a 1.5-million-row dataset returned in a couple of seconds."
  - "Seven export formats including **Parquet** and GeoJSON, plus a DCAT/RDF export of the whole catalogue. Municipal portals almost never ship columnar formats."
  - "Every dataset declares an intended update frequency against the EU frequency vocabulary, including 356 that honestly declare themselves one-off. Almost nobody does this."
weaknesses:
  - "The declared cadence lives only in the machine-readable DCAT layer. The portal's own `update_frequency` field is empty on all 702 datasets, so a human reading a dataset page is told nothing."
  - "Annual series are the weak spot: only 63.6% of datasets declaring ANNUAL are inside a generous 400-day window, and the 53 declaring IRREG make no testable promise at all."
  - "27.7% of fields carry a description, and 43% of datasets document no field at all. The English metadata is a fiction — 699 of 702 English titles are the Italian string copied over."

bestfor:
  - "Mobility, territory and sensor data for Bologna, where the feeds are genuinely live"
  - "Geospatial work — 300 datasets carry geometry and export as GeoJSON or SHP"
  - "Anyone who needs a municipal licence that will survive a legal review"
avoidfor:
  - "Assuming a dataset is maintained without reading its declared cadence first"
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

**And then there is the clock**, which is the part of this evaluation we got wrong first time and
which turns out to be the most interesting thing on the portal.

Every one of the 702 datasets declares an intended update frequency through
`dcat:accrualPeriodicity`, using the European Union's controlled frequency vocabulary. Not a
free-text note — a resolvable URI from a standard authority list. That is more than most national
statistical portals manage, and it means the catalogue can be held to its own word:

| Declared | Datasets | Median age | Inside its window |
|---|---:|---:|---:|
| DAILY | 16 | same day | 93.8% |
| WEEKLY | 7 | 6 days | 100% |
| MONTHLY | 127 | 14 days | 97.6% |
| QUARTERLY | 11 | 7 days | 100% |
| ANNUAL | 129 | 180 days | 63.6% |
| IRREG | 53 | 447 days | not testable |
| NEVER | 356 | 1,541 days | not applicable |

Of the 290 datasets that make a testable promise, **239 — 82.4% — are keeping it.** The
high-frequency feeds are close to perfect.

The single most important number in that table is **356 declared NEVER**. Half the catalogue is
explicitly flagged as one-off: a snapshot published once, never intended to be maintained. Those are
the datasets sitting at four and six years old, and they are not rot. They are doing exactly what
they said they would. A portal that admits half its holdings are frozen is being more honest than
one that quietly implies everything is live.

So the weakness is narrower than it looks, and it sits in two places. **Annual series are late**: only
63.6% of the 129 datasets declaring ANNUAL fall inside a generous 400-day window, so roughly a third
of Bologna's yearly statistical publishing has slipped its own deadline. And **53 datasets declare
IRREG**, which is a promise that cannot be broken because it does not say anything; their median age
is 447 days.

The real failure is one of audience. All of this lives in the machine-readable layer. The platform's
own `update_frequency` field — the one a human reading a dataset page would see — is empty on all
702. So a developer parsing DCAT knows precisely what to expect, and a journalist looking at the
same dataset in a browser is told nothing at all. Bologna has answered the question we posed in
[Fresh Is a Claim, Not a Property](/analyses/fresh-is-a-claim-not-a-property/), correctly and
completely, and then filed the answer where most of its readers will never look.

One small blemish for anyone harvesting: a dataset called `varco-n-65` carries the periodicity URI
`http://publications.europa.eu/rosurce/authority/frequencY/MONTHLY` — "rosurce" for "resource", and a
capital Y. A strict DCAT consumer will fail to resolve it. Four other datasets use `https` where the
remaining 698 use `http`.

The theme-by-theme staleness pattern still holds, and is worth stating because it explains *which*
datasets get declared NEVER: transport, environment and technology — the machine-pushed feeds — are
almost all current, while governance and administrative publishing carries the overwhelming majority
of the frozen snapshots. Automation keeps promises; human publishing schedules mostly get downgraded
to NEVER, honestly, and then stop.

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

**Grade B+.** The things Bologna decided once and automated are done better than most national
portals manage: one clean licence across 98.6% of the catalogue, no gate of any kind, seven export
formats including Parquet, and — the part we initially missed and were wrong about — a complete,
standards-based declaration of what every dataset intends to do. On that last point this is a model
municipal portal, and we should have said so first time.

What holds it back is not honesty but reach. The commitments are made to machines and withheld from
people; a third of the annual series are late against their own declaration; and below the dataset
description the documentation thins to almost nothing, with 43% of datasets explaining none of their
own fields.

The cheapest available upgrade has not changed, only its target. Mirror the DCAT periodicity into
the field a human actually sees, and put a data dictionary on the sensor feeds. Neither is a
publishing programme. Both are an afternoon.
