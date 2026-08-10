---
title: "Global Power Plant Database"
date: 2026-07-18
publishers: ["World Resources Institute"]
regions: ["Global"]
place: "Global"
places: ["Global"]
domains: ["Energy", "Climate"]
licenses: ["CC BY 4.0"]

source: "https://datasets.wri.org/datasets/global-power-plant-database"
version: "v1.3.0 (June 2021)"
temporal: "Commissioning years from the 1890s to 2021"
updated: "v1.3.0, June 2021"
cadence: "Dormant — no release since 2021"
formats: ["CSV"]
size: "~34,900 plants across 167 countries"
access: "Direct download, no registration"

verdict: "Still the fastest way to put every large power station on a map — as long as you accept the map stopped moving in 2021."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 2
  documentation: 8
  accessibility: 9
  licensing: 9
  interoperability: 8

strengths:
  - "One row per plant, one schema, 167 countries — the join key problem is solved for you."
  - "Every capacity figure carries a `source` and `url` field, so you can audit any single row back to a national register."
  - "Generation columns are clearly separated into reported (`generation_gwh_*`) and estimated (`estimated_generation_gwh_*`). The distinction is not hidden."
weaknesses:
  - "No release since v1.3.0 in June 2021. Every solar and wind farm commissioned since is simply absent."
  - "Coverage is capacity-biased: small and distributed generation falls below the collection threshold in most countries."
  - "`commissioning_year` is sparse and inconsistently sourced — usable for eyeballing a fleet, not for vintage analysis."

bestfor:
  - "Mapping the world's large generating fleet in an afternoon"
  - "Teaching, prototypes and back-of-envelope capacity mixes"
  - "A geocoded skeleton to hang better national data on"
avoidfor:
  - "Anything about the last five years of the energy transition"
  - "Emissions accounting that needs current, plant-level generation"
  - "Distributed and rooftop capacity of any kind"
---

## What it is

One CSV. Roughly 34,900 power stations, 167 countries, each with a location, a capacity in
megawatts, a primary fuel, and — where anyone could find one — a commissioning year and an owner.
WRI assembled it by harmonising national registers and regulator filings into a single schema, which
is precisely the work nobody else wanted to do and everybody needed done.

For most of the last decade it was the default answer to "where are the world's power plants?" It
earned that. The schema is legible on first read, the geolocation is good enough to map without
cleaning, and the fuel taxonomy is coarse but honest.

## How it holds up

The structural work holds up extremely well. Six years on, the columns still make sense, the
identifiers are stable, and the provenance fields mean you can trace a suspicious row back to the
national source that produced it. That last part is rarer than it should be, and it is the single
biggest reason this database still scores as well as it does.

What does not hold up is the clock. Version 1.3.0 landed in June 2021 and nothing has landed since.
In a sector that added record renewable capacity every year afterwards, a 2021 snapshot is not a
current picture of anything — it is a historical document. Solar is the worst hit: the fleet has
changed shape most where the collection threshold was already weakest.

The coverage bias deserves stating plainly. This is a database of *large* plants. Distributed
generation, rooftop solar, small hydro and most behind-the-meter capacity are out of scope in
practically every contributing country. If your question is about the long tail, this dataset cannot
see it and will not tell you so.

## Working with it

It is a well-formed CSV and it behaves like one. Load it, filter on `country_long`, and be careful
with two things: `estimated_generation_gwh_*` columns are model output, not measurement, and the
`other_fuel1/2/3` columns are the only place multi-fuel plants declare themselves — filtering on
`primary_fuel` alone will quietly mis-class a lot of co-firing capacity.

Attribution is CC BY 4.0, which is about as frictionless as a licence gets. Cite the version. Given
the dormancy, the version number is now the most important thing in your methods section.

## The call

Grade B+, and the plus is entirely for craft rather than currency. As a geocoded backbone for the
world's large generating fleet it remains excellent and nothing has replaced it as cleanly. As a
description of the grid in 2026 it is out of date in the exact places the energy transition is
moving fastest. Use it for the skeleton; get your recent capacity somewhere that is still shipping.
