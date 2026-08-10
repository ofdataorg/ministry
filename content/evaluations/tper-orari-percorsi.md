---
title: "TPER Bus Timetables and Routes"
date: 2026-07-30
publishers: ["Comune di Bologna — Innovazione Digitale e Dati"]
regions: ["Europe"]
place: "Bologna"
places: ["European Union", "Italy", "Emilia-Romagna", "Bologna"]
domains: ["Mobility"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/tper-vigente/"
temporal: "Current month only"
updated: "July 2026"
cadence: "Declares MONTHLY, and meets it"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX"]
size: "519,150 rows of trip-stop pairs"
access: "Direct download and API, no registration"

verdict: "GTFS flattened into a single wide table, which makes it easy to open in Excel and useless to every tool that already speaks GTFS."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 8
  documentation: 5
  accessibility: 9
  licensing: 9
  interoperability: 5

strengths:
  - "GTFS identifiers are preserved — `trip_id`, `stop_id`, `route_id`, `service_id`, `shape_id`, `stop_sequence` — so the relational structure can be rebuilt if you know the standard."
  - "Route geometry ships as real linestrings and stops as coordinates, so mapping needs no external join."
  - "Declares MONTHLY and delivers on it, which for a timetable is the cadence that matters."
weaknesses:
  - "**It is a denormalised GTFS extract rather than GTFS.** Every consumer with an existing transit toolchain has to un-flatten it, and the tools that would have read a GTFS zip directly cannot use this."
  - "`shape_linestring` and `geo_point_2d` are empty in 96.2% of rows — the geometry attaches to a handful of rows and is null everywhere else, which surprises anyone treating this as a spatial layer."
  - "Current month only. No history, no future service, so schedule change analysis is impossible from this source alone."

bestfor:
  - "Quick stop-level queries without standing up a GTFS pipeline"
  - "Mapping current route geometry for Bologna"
  - "Teaching examples where a single flat table beats a relational feed"
avoidfor:
  - "Journey planning or accessibility modelling — use the real GTFS feed"
  - "Schedule change or service-level trend analysis"
  - "Spatial work that assumes every row carries geometry"
---

## What it is

Bologna's bus network for the current month, published as a single flat table: 519,150 rows, each
pairing a trip with a stop in sequence, carrying route and service identifiers, the stop name, a
day-type (`FERIALE` or `SABATO`), and — sometimes — geometry.

The identifiers are the giveaway. `trip_id`, `stop_id`, `stop_sequence`, `route_id`, `service_id`,
`shape_id` are the primary and foreign keys of **GTFS**, the General Transit Feed Specification that
every transit application on earth already consumes. What this dataset publishes is GTFS run through
a join and exported as one wide table.

## How it holds up

**Preserving the GTFS identifiers was the right call** and it is what saves this dataset. Because
`trip_id` and `stop_sequence` survive intact, a competent user can reconstruct the relational
structure — group by trip, order by sequence, and you have the stop pattern back. Had those been
dropped in favour of row numbers, the file would be unrecoverable. They were not, and credit is due.

**But flattening a standard is a strange thing to do to it.** GTFS exists precisely so that transit
data is interoperable: OpenTripPlanner, Valhalla, R5, every routing engine and journey planner reads
a GTFS zip without configuration. This file cannot be fed to any of them. A user with an existing
transit pipeline must reverse the denormalisation to get back to what the publisher started with,
and a user without one gets a 519,150-row table where a 30,000-row `stop_times.txt` and a 400-row
`trips.txt` would have carried the same information with less duplication.

The trade is presumably deliberate — a flat CSV is openable in Excel by a council officer, and a
GTFS zip is not. That is a real audience with a real need. But the standard feed is what makes
transit data *useful*, and publishing the derivative instead of the original inverts the usual
advice. TPER does publish GTFS elsewhere; anyone doing serious work should go there.

**The geometry is a trap.** `shape_linestring` and `geo_point_2d` are populated in **3.8% of rows**
and empty in the other 96.2%. This is an artefact of the flattening: a shape belongs to a route, not
to every trip-stop pair, so it appears on a handful of rows and is null on the rest. Nothing says
so. A user who loads this as a spatial layer sees a nearly-empty geometry column and reasonably
concludes the data is broken.

**Coverage is one month.** `tper-vigente` means the current timetable, and there is no archive. Any
question about how service changed — a route cut, a frequency reduction, a new night bus — cannot be
asked of this dataset, because last month's version has been overwritten.

`giorno` carries only `FERIALE` and `SABATO` in our sample, with no Sunday or holiday service
visible, and nothing documents whether Sunday is absent from the network, folded into another
category, or simply not in the extract. Five of ten fields are documented; this is not one of them.

## Working with it

If you need journey planning, accessibility isochrones or anything a routing engine does, stop here
and fetch TPER's GTFS feed instead. This file is for lookups.

For lookups it works well: filter by `stop_name` or `route_id` and read off the sequence. Deduplicate
on `shape_id` before mapping, rather than filtering out null geometry row by row.

## The call

**Grade B.** Current, openly licensed, ungated, honestly scheduled and with its keys intact — as a
convenience extract it does its job and the monthly cadence is kept.

It loses ground for being a flattened copy of a standard that already had an ecosystem, for geometry
that is 96% null with no explanation, and for keeping only the current month of a timetable whose
history is the interesting part. Publish the GTFS zip alongside it and both audiences are served.
