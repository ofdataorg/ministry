---
title: "Origini di Bologna — Historic Building Survey"
date: 2026-07-30
publishers: ["Comune di Bologna"]
regions: ["Europe"]
place: "Bologna"
places: ["European Union", "Italy", "Emilia-Romagna", "Bologna"]
domains: ["Society", "Geospatial"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/origini-di-bologna/"
version: "Completed survey, processed 16 July 2020"
snapshot: 2026-07-30
temporal: "A survey of the medieval and early-modern city"
updated: "July 2020"
cadence: "Declares NEVER — a completed survey, not a maintained series"
formats: ["CSV", "JSON", "GeoJSON", "SHP", "Parquet"]
size: "3,475 houses in the historic centre; twelve companion layers"
access: "Direct download and API, no registration"

verdict: "A remarkable piece of architectural scholarship released as open data and then left to explain itself, which it cannot."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 7
  documentation: 3
  accessibility: 9
  licensing: 9
  interoperability: 5

strengths:
  - "Building footprints as real polygons, not points — this is a surveyed architectural dataset with geometry you can map and measure."
  - "Twelve companion layers cover towers, porticoes, churches, covered canals, lost buildings, streets and fields, so the medieval city can be reassembled from open data."
  - "Honest cadence: it declares NEVER, which is exactly right for a completed historical survey and better than pretending it is maintained."
weaknesses:
  - "**Nulls are encoded as the string `-`.** Every field is 0% empty and simultaneously full of hyphens, so naive null-counting reports perfect completeness on columns that are almost entirely blank."
  - "None of the 26 fields is documented, on a dataset whose columns are specialist architectural terms — `modiglioni`, `archivolti`, `mensoloni architravati` — that even Italian speakers will not all know."
  - "`modiglioni`, `scuderia_e` and `link3` contain a single distinct value across the whole sample: `-`. Three columns carrying no information at all."

bestfor:
  - "Historical urban morphology and architectural research on central Bologna"
  - "Mapping the medieval city — towers, porticoes, canals and lost buildings together"
  - "Heritage and conservation context work"
avoidfor:
  - "Any null analysis that trusts empty-string counts"
  - "Current building condition or ownership — this is a historical survey, not a cadastre"
  - "Assuming coverage beyond the historic centre without checking the companion layers"
---

## What it is

A surveyed architectural inventory of Bologna's historic centre: 3,475 houses, each with a polygon
footprint, an ancient and a modern street number, a count of storeys, and a set of architectural
features — arcades, architraves, archivolts, corbels — plus recorded historic uses such as stables,
hay lofts and workshops. It is one of twelve layers; the companions cover towers, porticoes,
churches and convents, covered and open canals, streets, orchards and meadows, major and minor
buildings, and buildings that no longer exist.

Taken together this is the medieval and early-modern city rendered as a geodatabase, released under
CC BY 4.0, free, with no registration. As an act of open cultural publishing it is genuinely
impressive, and it links out to `originebologna.com`, the scholarly project behind it.

## How it holds up

**The cadence declaration is correct and we want to reward it.** This dataset says NEVER, and NEVER
is the truthful answer for a completed historical survey. It was last processed in July 2020 — six
years ago — and that is not decay, it is a finished piece of work sitting where it was left. A
portal that lets a publisher say "this is done" is a portal that lets its readers tell the
difference between finished and abandoned. Half of Bologna's catalogue declares NEVER, and this is
what the honest use of that value looks like.

**The null encoding is a genuine trap.** Every column reports 0% empty. Every column is also full of
`-`. The hyphen is the survey's placeholder for "not recorded" or "not applicable", written into the
data as a literal string, so any standard completeness check — `isnull()`, `COUNT(*) WHERE x IS
NULL`, a profiling tool's missing-value report — returns a perfect score on a dataset that is mostly
blank in its detail columns.

Three columns contain nothing else at all. `modiglioni`, `scuderia_e` and `link3` have exactly one
distinct value across our sample: `-`. They are empty columns wearing a full-data disguise. And
`name`, the building name, is `-` for the overwhelming majority of the 3,475 houses; only 131
distinct names exist.

**None of the 26 fields is documented,** and this is the dataset where that hurts most. The columns
are specialist architectural vocabulary — `modiglioni` (corbels), `archivolti` (archivolts),
`mensoloni_architravati` (architraved brackets), `architravate_con_colonne_di_legno` (architraved
with wooden columns). These are terms from Italian architectural history. Their values are integers,
so presumably counts of each feature per building, but nothing says whether a `2` under `arcate`
means two arches on the façade, two bays, or something else entirely. The scholarship that produced
these categories exists. It is not attached to the file.

**Interoperability is mid.** Polygons ship as proper `geo_shape` alongside centroids, and SHP and
GeoJSON exports work — so the spatial side is fine. It is the attribute side, with its string nulls
and undefined vocabulary, that costs it.

## Working with it

Replace `-` with a real null on load, before anything else. Then re-run your completeness check and
work from the real picture rather than the flattering one.

Take the companion layers together; the value here is the assembled city, not one table. Follow the
`link1` URLs into `originebologna.com` for the interpretive material the dataset omits — that is
where the definitions actually live.

## The call

**Grade B.** A scholarly asset published openly, geometrically sound, and honest about being
finished — the instinct to release this at all is the right one and the NEVER declaration is a model
for how to retire a dataset without deleting it.

What it lacks is the survey's own key. Twenty-six architectural terms, a hyphen convention, and a
sentence about what the integers count would turn a specialist curiosity into a usable research
dataset. That documentation was written once, for the project this came from. It just never made it
into the file.
