---
title: "Bologna Bicycle Counters"
date: 2026-07-30
publishers: ["Comune di Bologna"]
regions: ["Europe"]
domains: ["Mobility"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/colonnine-conta-bici/"
temporal: "Hourly counts, multi-year rolling history"
updated: "Same day"
cadence: "Declares MONTHLY, delivers daily"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX"]
size: "519,392 hourly observations from 19 counter posts"
access: "Direct download and API, no registration"

verdict: "Half a million hours of cycling counts, directional and geolocated, described in a 237-character sentence."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 10
  documentation: 4
  accessibility: 9
  licensing: 9
  interoperability: 7

strengths:
  - "Directional counts — inbound and outbound are separate columns, which is what makes commute-pattern analysis possible at all."
  - "Hourly resolution over several years from a fixed array, so seasonality, weather response and modal-shift trends are all in reach."
  - "Declares MONTHLY and actually publishes daily. Under-promising and over-delivering is the right way round."
weaknesses:
  - "The dataset description is 237 characters, and `colonnina` and `geo_point_2d` — the identity and the location of each counter — are undocumented."
  - "`direzione_centro` and `direzione_periferia` carry the *identical* description, `Direzione bicicletta`, which distinguishes neither."
  - "`totale` is 100% redundant with the sum of the two direction columns across every row we tested — a derived column shipped as an observation."

bestfor:
  - "Cycling volume trends and commute directionality in Bologna"
  - "Weather, season and intervention impact studies with a clean hourly baseline"
  - "Before-and-after evaluation of cycle infrastructure at instrumented corridors"
avoidfor:
  - "City-wide cycling estimates — this is 19 posts at 15 locations"
  - "Treating a zero as an absence of cycling rather than a possible counter outage"
  - "Assuming counter names map one-to-one to physical sites"
---

## What it is

Hourly bicycle counts from Bologna's automatic counting posts: a timestamp, an inbound count
(`direzione_centro`), an outbound count (`direzione_periferia`), a total, the name of the post, and
a coordinate. 519,392 observations from 19 named counters.

Directional counting is the feature that matters. A single volume number tells you how busy a route
is; splitting it by direction tells you when the city commutes, which corridors are asymmetric, and
whether a new cycle lane shifted flow or merely moved it. Bologna publishes the split, hourly, going
back years, and updates it daily.

## How it holds up

**Timeliness is exemplary and the promise structure is the right way round.** The dataset declares
MONTHLY through `dcat:accrualPeriodicity` and publishes daily. We would rather see a conservative
declaration comfortably beaten than an ambitious one missed, and after finding that a third of
Bologna's ANNUAL series run late, this one is a relief.

**Documentation is where it thins out.** The dataset description runs to 237 characters — barely two
sentences for a half-million-row behavioural dataset. Four of six fields carry a description, but
the quality of those descriptions is the real problem: `direzione_centro` and `direzione_periferia`
are both documented as *"Direzione bicicletta"*. The same four words, for the two columns whose
distinction is the entire analytical value of the dataset. A reader has to infer from the column
names that one means toward the centre and the other away from it. That inference is almost
certainly correct and it should not be an inference.

`colonnina` and `geo_point_2d` are undocumented entirely, which matters more than it sounds.
Nineteen counter names resolve to **fifteen distinct coordinates**: four locations host two names
each — `Massarenti_I` and `Massarenti_II` sit at identical coordinates, and the same pattern repeats
three more times. Almost certainly these are paired posts on opposite sides of a road or separate
lanes at one junction. Nothing says so. Anyone grouping by coordinate will silently merge two
counters; anyone grouping by name will treat one site as two.

**`totale` is redundant.** Across 3,000 tested rows there is not a single case where `totale` differs
from `direzione_centro + direzione_periferia`. Zero mismatches. This is the same habit we found in
the [parking sensor feed](/evaluations/bologna-parcheggi-trento-trieste/), where `status` is fully
derivable from `detectedobjects` — a portal-wide tendency to ship computed columns alongside the
inputs they are computed from. It is harmless if you know, and it invites double-counting if you do
not.

## Working with it

Group by `colonnina`, not by coordinate, and treat the `_I`/`_II` suffixed pairs as a single site
when you want per-location totals. Drop `totale` and compute it yourself.

Be careful with zeros. A zero-count hour at 04:00 is entirely plausible; a run of zero-count hours
mid-afternoon is more likely an outage. Nothing in the schema distinguishes "counted nothing" from
"was not counting", so flag suspicious runs before modelling.

## The call

**Grade B+.** A genuinely valuable behavioural dataset, live, directional, openly licensed and
free — the substance is strong and the refresh discipline is better than the portal average. It is
held back by two sentences of description where a page is needed, a duplicated field definition on
the only two columns that matter, and an undocumented naming scheme that will cost every new user
the same hour.
