---
title: "Città Metropolitana di Milano — Resident Population by Age (2018)"
date: 2026-08-10
publishers: ["Città Metropolitana di Milano"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Population"]
licenses: ["CC0 1.0"]

source: "https://www.dati.lombardia.it/d/7fhb-due2"
version: "31 December 2018 snapshot — 133 rows, published November 2019"
snapshot: 2026-08-10
temporal: "31 December 2018"
updated: "15 November 2019"
cadence: "Declares Mai (never) — a one-off snapshot"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "133 municipalities, 106 columns"
access: "Open API and bulk download, no registration"

verdict: "One hundred and one columns named `_0` to `_100`, one for each year of age, because somebody exported a spreadsheet."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 3
  documentation: 2
  accessibility: 9
  licensing: 9
  interoperability: 3

strengths:
  - "Complete for its scope: every one of the 133 municipalities in the metropolitan area, by single year of age."
  - "CC0 — a public domain dedication, with nothing to comply with."
  - "Carries `codice_istat` and `codice_catastale` alongside the municipality name, so it joins cleanly despite everything else."
weaknesses:
  - "**101 of its 106 columns are named `_0`, `_1`, `_2` … `_100`** — one per year of age, in the field names, with no documentation."
  - "Single-year snapshot, published once and never revisited, so the series that would make it useful has to be assembled from separate unlinked datasets."
  - "Zero of 106 columns documented, which for the five that are not ages leaves `zona_omogenea` unexplained."

bestfor:
  - "Age structure of Milan metropolitan municipalities at end-2018, after reshaping"
  - "A denominator for 2018 rates in the metropolitan area"
avoidfor:
  - "Loading into anything that expects tidy data"
  - "Current population figures"
  - "Time series, without collecting the other yearly editions separately"
---

## What it is

The resident population of each municipality in the Città Metropolitana di Milano at 31 December
2018, broken down by single year of age. 133 rows — one per municipality — and 106 columns.

The arithmetic gives the problem away. 133 rows and 106 columns, for a table whose real dimensions
are municipality × age. It is a spreadsheet, exported.

## How it holds up

**The data is right and the shape is wrong.** Of the 106 columns, **101 are named `_0` through
`_100`** — one per year of age, with the age encoded in the column name. The display labels are bare
numbers: `7`, `36`, `78`. The remaining five are `comune`, `codice_istat`, `codice_catastale`,
`zona_omogenea` and a sort key.

This is the widest example of report-shaped publishing in the catalogue, and it is worse than the
[24 hourly columns](/evaluations/bologna-accuratezza-spire/) we criticised in Bologna because the
column names carry data. Every consumer's first operation is melting a hundred columns into two —
`eta` and `residenti` — and the melt has to strip a leading underscore from the field name to
recover the age as a number. Nothing about that is difficult; it is simply work imposed on every
user, forever, to save one transformation at publication.

It also makes the file fragile. A column named `_0` sorts next to `_1` and `_10`, not next to `_1`
numerically, so any tooling that iterates columns in lexical order silently scrambles the age
ordering.

**Documentation is zero of 106.** For the age columns that is almost defensible, since the name
carries the meaning once you have guessed the convention. For `zona_omogenea` — the homogeneous
zone, an administrative grouping used in metropolitan planning, with values like *Magentino
Abbiatense* — it is not. Nothing explains what the zones are or where the boundaries come from.

**On timeliness it is honest and thin.** `Mai` is the right label for a dated snapshot and we credit
it. But population by age is only interesting as a series, and this is one year, published once. The
other years exist as separate datasets with no stated relationship, so building a series means
finding them and hoping the schema held.

**The licence is exemplary**: CC0, no conditions.

## Working with it

Melt on load. Take the columns matching `^_\d+$`, strip the underscore, cast to integer age, and you
have a tidy table of municipality, age, count in about four lines. Then join on `codice_istat`
rather than the municipality name.

Do not trust column order. Sort ages numerically after the melt.

## The call

**Grade C+.** The underlying statistics are ISTAT-derived and sound, the coverage is complete for the
metropolitan area, and the licence is the best available. Everything else about how it was published
works against the reader: a hundred data-bearing column names, no documentation, and a single year
stranded from its own series.

Publishing the same numbers in long form — three columns instead of a hundred and six — would raise
the interoperability score from 3 to 8 and change nothing else about the file.
