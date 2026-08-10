---
title: "NDAP — India's National Data and Analytics Platform"
date: 2026-04-15
publishers: ["NITI Aayog"]
regions: ["Asia"]
places: ["India"]
domains: ["Economy", "Population", "Governance"]
licenses: ["Government Open Data Licence — India"]

source: "https://ndap.niti.gov.in/"
temporal: "Varies by source dataset"
updated: "Rolling, per contributing ministry"
cadence: "Inconsistent — follows each publisher"
formats: ["CSV", "API (JSON)"]
size: "Hundreds of datasets from central and state government sources"
access: "Free; registration required for bulk download and API"
verdict: "A serious attempt to make India's fragmented official statistics joinable, still limited by the ministries feeding it."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 6
  documentation: 7
  accessibility: 7
  licensing: 6
  interoperability: 8

strengths:
  - "Standardised administrative geography codes across datasets — the single most useful thing anyone has done for Indian data reuse."
  - "Time and geography dimensions are normalised at ingestion, so cross-ministry joins are possible without manual reconciliation."
  - "Dataset pages carry source attribution, coverage notes and update dates rather than dumping a bare file."
weaknesses:
  - "Coverage depends entirely on what ministries choose to contribute; large areas of official statistics are still absent."
  - "Update cadence is inherited from the source, so freshness varies from months to years with no consistent signal."
  - "Registration gating and an open-government licence with usage conditions make automated and commercial reuse more awkward than it needs to be."

bestfor:
  - "Cross-ministry analysis where district codes must line up"
  - "A first stop before chasing individual ministry portals"
  - "District-level indicators with documented provenance"
avoidfor:
  - "Comprehensive coverage of Indian official statistics"
  - "Anything requiring guaranteed currency"
  - "Frictionless commercial pipelines"
---

## What it is

NDAP is NITI Aayog's platform for pulling datasets from across central and state government into one
place with a common structure. The pitch is not "more data" — most of it existed on ministry
portals already — but *joinable* data: consistent geography codes, normalised time dimensions, and
enough metadata to know what you are holding.

Anyone who has tried to join an Indian health indicator to an economic one at district level knows
exactly why this platform exists. The traditional experience involves three portals, two spellings
of every district, and an afternoon spent on a manual crosswalk.

## How it holds up

Interoperability is the highest score here and it is the whole point of the platform. Standardising
administrative geography at ingestion is unglamorous plumbing, and it converts a class of analysis
from "possible with effort" to "possible". District codes that line up across ministries are worth
more than another hundred datasets would be.

Documentation is decent. Dataset pages state the source, the coverage, the period and the last
update, which is more context than most national portals bother with.

Completeness is where the ceiling sits, and it is not really NDAP's ceiling. The platform holds
what ministries send it. Substantial parts of Indian official statistics — including some of the
most-requested survey microdata — are not there, and the platform cannot compel their release. The
result is a catalogue that is genuinely useful and visibly partial, and a user journey that often
ends with "and now go to the ministry site anyway".

Timeliness inherits the same problem in a more confusing form. Because each dataset follows its
source publisher's schedule, freshness ranges from recent to several years old with no consistent
indicator of which regime you are in. Read the update date on every page. Do not assume the platform
implies currency.

Licensing is workable but not frictionless: the Government Open Data Licence — India permits reuse
with attribution and conditions, and bulk access is gated behind registration. Neither is unusual
for a government portal; both add process to automated pipelines.

## Working with it

Start here for anything that needs district-level joins, and treat the standardised geography codes
as the primary reason to be here. Check each dataset's update date individually rather than trusting
the catalogue. When something you need is missing, expect the underlying ministry portal to be the
fallback, and expect its geography codes to disagree with NDAP's.

## The call

Grade B. The design instinct is right and the geography standardisation genuinely improves what is
possible with Indian public data. It is held back by partial ministry participation, inherited and
uneven update cadences, and access friction. As the contribution base grows this could move up
substantially — the platform is not the bottleneck.
