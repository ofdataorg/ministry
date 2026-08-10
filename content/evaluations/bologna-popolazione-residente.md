---
title: "Bologna Resident Population Series"
date: 2026-07-30
publishers: ["Comune di Bologna — U.I. Ufficio Comunale di Statistica"]
regions: ["Europe"]
place: "Bologna"
places: ["European Union", "Italy", "Emilia-Romagna", "Bologna"]
domains: ["Population", "Society"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/popolazione-residente-per-stato-civile-eta-sessocittadinanza-quartiere-e-zona-se/"
temporal: "Annual series from 1986"
updated: "May 2025"
cadence: "Declares ANNUAL — 429 days since last processing, so currently late"
formats: ["CSV", "JSON", "Parquet", "XLSX"]
size: "551,981 rows"
access: "Direct download and API, no registration"

verdict: "Forty years of Bologna's population cross-cut six ways in a perfectly tidy table, with not one word explaining any of it."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 5
  documentation: 3
  accessibility: 9
  licensing: 9
  interoperability: 8

strengths:
  - "Genuinely tidy: one row per year, citizenship, age, district, zone, marital status and sex, with a single `residenti` count. No pivoting, no melting, no repair."
  - "Three parallel age encodings — single year, five-year bands and broad groups — shipped together, so most analyses need no recoding."
  - "Annual series from 1986. Four decades of small-area demographic change for a major European city, free and ungated."
weaknesses:
  - "**Zero of 11 fields documented.** Not one line on residence definitions, the treatment of `Z. Senza fissa dimora`, or how the boundaries were handled across four decades of administrative reorganisation."
  - "Declares ANNUAL and was last processed 429 days ago, so the series has slipped its own commitment — as have a third of Bologna's annual datasets."
  - "The `zona` and `quartiere` labels are shipped as text with no stable codes, so joins to boundary files rely on string matching."

bestfor:
  - "Small-area demographic analysis of Bologna over four decades"
  - "Ageing, household formation and migration trend work at district level"
  - "A denominator for any per-capita rate in the rest of the catalogue"
avoidfor:
  - "Current-year population figures — it is over a year behind its own schedule"
  - "Cross-district comparison across long spans without checking boundary changes"
  - "Anything sensitive to the exact definition of residence, which is undocumented"
---

## What it is

Bologna's resident population, annually since 1986, cross-tabulated by citizenship (Italian or
foreign), single year of age, five-year band, broad age group, district, zone, centre-versus-
periphery, marital status and sex. 551,981 rows, one integer count in each.

This is the statistical backbone of the city. Almost every rate anyone computes about Bologna —
crime per capita, cycling per resident, complaints per thousand — needs a denominator, and this is
it, at a spatial resolution most cities do not publish and a time depth almost none do.

## How it holds up

**The structure is excellent and deserves specific praise.** This is a properly tidy table: one
observation per row, one variable per column, a single measure. After the wide, stringly-typed
layouts elsewhere on this portal — [24 hourly columns of percentage text](/evaluations/bologna-accuratezza-spire/)
being the worst offender — arriving at a file that loads correctly with default settings and needs
no reshaping is a relief.

Shipping three age encodings together is a small, thoughtful decision that saves every user the same
recoding step. Whoever built this understood who was going to use it.

**And then it explains nothing at all.** Zero of eleven fields carry a description. The dataset
description runs to 473 characters.

For most datasets that would be a documentation complaint. For an official demographic series it is
a methodological one, because population statistics are definitional all the way down. What counts
as resident — registered residence, or presence? How are people counted in the year they arrive or
die? What exactly is `Z. Senza fissa dimora`, the "no fixed abode" zone that appears alongside
Centro Storico and the periphery as a third value of the centre/periphery split — and what does it
mean for rates computed by zone? Is `Straniera` citizenship at the point of measurement, so that
naturalisation moves a person between categories without anyone migrating?

Every one of those questions changes what a published figure means. The Ufficio Comunale di
Statistica knows all the answers. None of them are here.

**Boundaries are the second methodological gap.** Forty years of a series covering districts and
zones, and Bologna's administrative geography has been reorganised in that period — the city moved
from nine districts to six in 2016. The dataset ships district and zone as free text with no
codes and no vintage marker, so a user building a 1986-to-2024 panel by district is string-matching
across a boundary change that the file does not mention. This is precisely the trap we described in
the [Eurostat evaluation](/evaluations/eurostat-database/), where regional series fracture silently
across geography revisions.

**Timeliness is the weak axis.** The dataset declares ANNUAL and was last processed in May 2025 —
429 days before we looked. It has missed its own stated cadence, and it is not alone: only 63.6% of
Bologna's ANNUAL datasets sit inside a generous 400-day window.

## Working with it

Load it as-is; it will behave. Pin the `anno` values you need and check that district labels are
consistent across the span before you group by them — if a label appears in some years and not
others you have found a boundary change, not a depopulated district.

For anything published, contact the statistics office about the residence definition. They will
answer; the file will not.

## The call

**Grade B.** As a data structure this is among the best-shaped things on the portal and it is the
denominator half the catalogue needs. It is held back by a complete absence of methodological
documentation on a series where definitions decide the answer, by untracked boundary changes across
four decades, and by an annual commitment it is currently over a year late against.

The fix is not technical. It is a page of notes from the office that already produced the numbers.
