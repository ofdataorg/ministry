---
title: "Humanitarian Data Exchange (HDX)"
date: 2026-04-02
publishers: ["UN OCHA Centre for Humanitarian Data"]
regions: ["Global", "Africa", "Asia"]
place: "Global"
places: ["Global"]
domains: ["Humanitarian", "Governance"]
licenses: ["Mixed — per contributing organisation"]

source: "https://data.humdata.org/"
temporal: "Varies by dataset; heaviest coverage from 2014"
updated: "Continuously"
cadence: "Per contributor; some datasets live, many dormant"
formats: ["CSV", "XLSX", "GeoJSON", "Shapefile"]
size: "Tens of thousands of datasets across active crisis contexts"
access: "Open, no registration"
verdict: "The right catalogue in the right places, holding a lot of files that stopped being maintained the day the funding did."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 6
  documentation: 5
  accessibility: 9
  licensing: 5
  interoperability: 5

strengths:
  - "For many crisis contexts, this is the only place administrative boundaries, population baselines and response data exist together."
  - "No registration, no gate, clean download URLs, a working API."
  - "The HXL hashtag standard is a genuinely clever, low-friction way to make heterogeneous spreadsheets machine-readable."
weaknesses:
  - "Quality control is contributor-side. A meticulously maintained boundary file and an abandoned 2017 assessment sit side by side with identical presentation."
  - "Licences are set per contributor and range from CC0 to bespoke terms to nothing stated at all."
  - "HXL adoption is partial, so the standard that would make bulk processing possible only covers some of the catalogue."

bestfor:
  - "Administrative boundaries and population baselines for crisis contexts"
  - "Finding out who has published what in a given emergency"
  - "Rapid situational work where nothing better exists"
avoidfor:
  - "Assuming catalogue presence implies current maintenance"
  - "Bulk automated ingestion without per-dataset licence checks"
  - "Comparative analysis across contexts with heterogeneous sources"
---

## What it is

HDX is OCHA's open catalogue for humanitarian data: administrative boundaries, population
statistics, displacement figures, health facility lists, needs assessments and response monitoring,
contributed by UN agencies, NGOs, governments and research organisations. In many crisis contexts it
is not the best source — it is the only one.

## How it holds up

Accessibility is excellent and should be praised without qualification. No registration, no
click-through, stable download links, a working API, and a search that finds things. For people
working under time pressure in bad conditions, that is the thing that matters most, and HDX gets it
right.

The rest of the scorecard reflects what a catalogue can and cannot control.

HDX does not produce data; it hosts what others contribute, and the quality varies enormously.
A carefully maintained COD (Common Operational Dataset) boundary file for an active response and a
one-off needs assessment abandoned in 2017 appear in the same search results with the same visual
weight. The metadata records an update date, which helps, but nothing signals *maintenance
intent* — whether anyone is still looking after a file. Users routinely mistake presence for
currency, and the interface does not push back.

Licensing is the sharpest practical problem. Terms are set per contributing organisation and span
CC0, CC BY, custom humanitarian terms, and a meaningful number of datasets with no clear licence at
all. Any project that ingests HDX in bulk inherits a legal audit it probably has not planned for.
The catalogue has grown faster than licence hygiene has.

HXL deserves specific credit. Adding standardised hashtags in a header row so a spreadsheet becomes
machine-readable without restructuring is a genuinely smart piece of design that meets contributors
where they are. Its weakness is arithmetic: partial adoption means you cannot rely on it, so
pipelines end up handling both HXL-tagged and untagged files anyway.

## Working with it

Prefer the Common Operational Datasets — the COD boundaries and population figures are the
maintained core of the catalogue and are curated to a real standard. For everything else, read the
update date and the contributing organisation before the file itself, and treat anything over a
year old in an active context as historical rather than current. Record the licence per dataset at
ingestion time, not later.

## The call

Grade B−. Accessibility is close to exemplary and in many contexts this catalogue is genuinely
irreplaceable. The score is dragged down by contributor-dependent quality with no maintenance
signal, a licence patchwork that makes reuse a legal exercise, and a good interoperability standard
that only half the catalogue speaks. Start from the CODs and verify outward.
