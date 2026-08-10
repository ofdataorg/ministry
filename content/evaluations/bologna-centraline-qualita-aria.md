---
title: "Bologna Air Quality Stations"
date: 2026-07-30
publishers: ["Comune di Bologna"]
regions: ["Europe"]
place: "Bologna"
places: ["European Union", "Italy", "Emilia-Romagna", "Bologna"]
domains: ["Environment", "Health"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/centraline-qualita-aria/"
temporal: "Rolling daily measurements; a separate historic series runs from 2000"
updated: "Same day"
cadence: "Declares DAILY, and meets it"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX"]
size: "45,302 measurements across three monitoring stations"
access: "Direct download and API, no registration"

verdict: "Every field documented, updated daily, and it still will not tell you what unit the number is in."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 10
  documentation: 6
  accessibility: 9
  licensing: 9
  interoperability: 6

strengths:
  - "All five fields carry a description — one of only a minority of Bologna datasets that documents itself at all."
  - "Declares DAILY through `dcat:accrualPeriodicity` and delivers same-day. Air quality is exactly the kind of data where that matters."
  - "Long, tidy shape: one row per station, per pollutant, per timestamp. No pivoting required."
weaknesses:
  - "**There is no unit of measure anywhere in the dataset.** Eight different pollutants share a single `value` column and nothing states whether it is µg/m³, mg/m³ or ppb."
  - "Three stations for a city of 400,000. Porta San Felice, Giardini Margherita and Via Chiarini, and that is the whole network."
  - "The historic companion dataset carries a `um` column that this one drops, so the live feed is less self-describing than the archive it continues."

bestfor:
  - "Daily pollutant tracking at three fixed Bologna sites"
  - "Teaching examples that need a small, clean, genuinely live environmental feed"
  - "Joining to the historic series for long-run trend work"
avoidfor:
  - "Any published figure where the unit matters and you have not verified it against ARPAE"
  - "Spatial interpolation across the city from three points"
  - "Regulatory or health-threshold comparison without independent confirmation"
---

## What it is

Daily air quality measurements from Bologna's monitoring stations: an identifier, a timestamp, a
station name, a measured value, and the pollutant it refers to. Eight pollutants appear —
NO₂, O₃, NOₓ, and the rest of the usual regulatory set — across three stations, in a clean long
format that needs no reshaping.

It is one of the better-behaved datasets in the [Bologna catalogue](/evaluations/comune-di-bologna-open-data/).
It declares DAILY and it delivers daily. Every one of its five fields has a description, which puts
it in the minority of a portal where 43% of datasets document nothing at all.

## How it holds up

**Timeliness is a straight ten** and this is the right dataset to give it to. Air quality data that
arrives a month late is a historical curiosity; air quality data that arrives today is something a
person with asthma can act on. Bologna publishes it today.

**And then the unit is missing.** The five documented fields are `id`, `reftime`, `stazione`,
`value` and `agente_atm`. The description of `value` reads, in full, *"Valore misurato
dell'agente"* — the measured value of the agent. Of what? A column that mixes NO₂ and ozone
readings in a single numeric field, with eight different pollutants that are conventionally reported
in different units and at wildly different magnitudes, and no unit column and no statement in the
documentation.

This is not a pedantic complaint. Ozone and nitrogen dioxide are both usually reported in µg/m³ in
the European regulatory framework, so a knowledgeable user can make an educated assumption — but
making an educated assumption is precisely what a data dictionary exists to prevent. The historic
companion dataset, `dati-centraline-bologna-storico`, ships a `um` column carrying exactly this
information. The live feed dropped it. A dataset should not be less self-describing than the archive
it continues.

**Coverage is thin and honest about it.** Three stations. That is the network Bologna operates, not
a subset the portal has withheld, so we do not penalise it heavily — but three points cannot
characterise pollution across a city with a ring road, a historic centre with restricted traffic,
and a large industrial periphery. Anyone tempted to interpolate a surface from this should not.

## Working with it

Join it to the historic series on station and pollutant to recover the unit, and carry that unit
forward explicitly in your own schema. If the number matters, verify against ARPAE Emilia-Romagna,
which operates the regional monitoring network and publishes the authoritative figures.

Watch `reftime`: values arrive as the previous day at 22:00 UTC, which is midnight local time in
summer. Naive date extraction in UTC will assign readings to the wrong day for anyone working in
Italian local time.

## The call

**Grade B+.** Live, documented, tidy, openly licensed and free — this is a municipality doing the
job properly and it deserves the credit. The missing unit is a one-line fix that would take the
documentation score from a six to an eight, and it is the only thing standing between this and a
dataset you could publish a health finding from without a phone call to check what you are holding.
