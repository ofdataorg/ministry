---
title: "Bologna Traffic Loop Accuracy"
date: 2026-07-30
publishers: ["Comune di Bologna"]
regions: ["Europe"]
domains: ["Mobility", "Governance"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/accuratezza-spire-anno-2025/"
temporal: "One dataset per year, 2022 onward"
updated: "January 2026 for the 2025 edition"
cadence: "Declares NEVER — each year is a closed snapshot"
formats: ["CSV", "JSON", "Parquet", "XLSX"]
size: "335,866 daily accuracy records across roughly 920 loops"
access: "Direct download and API, no registration"

verdict: "A city publishing the measured reliability of its own traffic sensors is doing something almost nobody does — in twenty-four columns of percentage strings."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 6
  documentation: 5
  accessibility: 9
  licensing: 9
  interoperability: 3

strengths:
  - "**Bologna publishes the accuracy of its own instruments.** Almost no city publishes a quality metric against its own sensor network, and it is what makes the underlying traffic counts usable."
  - "Hourly granularity, daily rows, roughly 920 loops, and a consistent annual series from 2022 onward."
  - "`codice_spira_2` is documented with an honest caveat — the loop identifier *can change over time* — which is exactly the kind of warning most publishers omit."
weaknesses:
  - "**Twenty-four columns, one per hour.** The wide layout is a spreadsheet artefact that every consumer has to melt before doing anything."
  - "Accuracy values are text strings with a percent sign — `'100%'`, `'0%'` — so nothing is numeric until you strip and cast."
  - "Negative values appear (`-1%`), which is not a percentage of anything and is almost certainly a sentinel for missing data. Nothing documents it."

bestfor:
  - "Weighting or filtering Bologna's traffic loop counts by measured reliability"
  - "Sensor-network health and maintenance analysis"
  - "A rare worked example of a public body auditing its own instruments in public"
avoidfor:
  - "Loading directly into anything that expects tidy data"
  - "Treating `-1%` as a low accuracy score rather than a missing reading"
  - "Linking loops across years without handling identifier changes"
---

## What it is

For every inductive traffic loop in Bologna, for every day of the year, the measured accuracy of
that loop in each hour of the day. 335,866 rows for 2025 alone, roughly 920 loops, with matching
datasets for 2022, 2023 and 2024.

Start with the credit, because it is substantial. Traffic loop counts are the raw material of urban
mobility analysis, and every one of them carries an error rate that most cities never measure and
almost none publish. Bologna measures it and puts it on the open portal next to the counts
themselves. That is a publisher inviting scrutiny of its own instruments, and it is rare enough that
it deserves to be said before any criticism.

It is also, on paper, the best-documented dataset in the entire
[Bologna catalogue](/evaluations/comune-di-bologna-open-data/) — 26 of 27 fields carry a
description, against a portal average of 27.7%.

## How it holds up

**The documentation is a coverage statistic, not a content one.** Those 26 descriptions are: one for
the date, one genuinely useful note on the loop identifier, and then the same two words —
*"fascia oraria"*, time band — repeated twenty-four times, once for each hourly column. Technically
every field is documented. Substantively, the file tells you that the column named `08_00_09`
covers a time band, which the column name already said.

The one description that earns its place is on `codice_spira_2`, which warns that the loop code
*può cambiare nel tempo* — can change over time. That is a real caveat with real consequences for
anyone building a multi-year panel, and the publisher volunteered it. It is the single best line of
documentation we have read on this portal, and it sits in a file that otherwise says nothing.

**The shape is the problem.** Twenty-four hourly columns is a report layout, not a dataset layout.
Every consumer's first operation is melting 24 columns into two, and the file is four times larger
than the long form would be. This is the "spreadsheets built for eyes" failure we scored
[e-Stat](/evaluations/e-stat-japan/) down for, in a milder form.

Then the values. Accuracy arrives as text — `'100%'`, `'0%'`, `'91%'` — with the percent sign
inside the string, so the column is unusable until stripped and cast. And among the values are
negatives: `-1%` appears throughout. A negative accuracy percentage is not a measurement of
anything. It is a sentinel, almost certainly meaning "no reading available", and nothing in the
documentation says so. A consumer who casts naively and averages will pull their fleet-wide accuracy
figure downward with values that are not observations.

**Timeliness sits mid.** The 2025 edition was processed in January 2026, which is prompt for an
annual close. It declares NEVER, which is honest for a closed yearly snapshot, though it means the
series is a set of unlinked files rather than a maintained resource — and given that loop
identifiers change between years, joining them is the user's problem.

## Working with it

Melt the 24 hour columns immediately. Strip `%`, cast to numeric, and map anything negative to null
before you compute a single statistic. Then join to the traffic count data and use accuracy as a
weight or a filter rather than ignoring it, which is the whole reason this dataset exists.

For multi-year work, do not assume `codice_spira_2` is stable. The publisher has told you it is not.

## The call

**Grade B.** The instinct here is genuinely admirable and we would like more cities to copy it —
publishing the error rate of your own sensors is an act of confidence. The execution is a report
exported to CSV: wide, stringly-typed, with an undocumented sentinel in the middle of the numbers.

Melt it to long form, ship the values as floats, and document what `-1` means. That is an afternoon,
and it would take this from a B to somewhere near the top of the catalogue.
