---
title: "ARPA Lombardia — Rainfall from 2021"
date: 2026-08-10
publishers: ["ARPA Lombardia"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Environment", "Climate"]
licenses: ["CC0 1.0"]

source: "https://www.dati.lombardia.it/d/pstb-pga6"
version: "67,262,315 readings at snapshot; series from 1 January 2021"
snapshot: 2026-08-10
temporal: "1 January 2021 onward"
updated: "6 March 2026"
cadence: "Declares semestrale (six-monthly), and keeps it"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "67,262,315 readings, 4 columns"
access: "Open API and bulk download, no registration"

verdict: "Sixty-seven million rain gauge readings at ten-minute resolution, none of which say where they were taken."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 7
  documentation: 5
  accessibility: 8
  licensing: 9
  interoperability: 6

strengths:
  - "**67.3 million readings at up to ten-minute resolution** from the regional hydro-meteorological network — the largest dataset we have measured anywhere on this site."
  - "All four columns documented, and it declares a six-monthly cadence which it actually keeps."
  - "CC0 on a full environmental monitoring series, which is close to the best licensing outcome available for sensor data."
weaknesses:
  - "**No location.** `idsensore` is an integer, and nothing in the file says where that sensor is. Every spatial use requires a separate station registry that is not linked from here."
  - "`stato` carries validation codes such as `VA` with no vocabulary — so the boundary between a validated reading and a provisional one is undocumented."
  - "Six-monthly publication on a ten-minute sensor stream means the freshest data can be six months old, which rules out operational use."

bestfor:
  - "Climatological and hydrological analysis across Lombardia since 2021"
  - "Extreme rainfall and return-period work at high temporal resolution"
  - "Any study that can afford to join the station registry itself"
avoidfor:
  - "Flood warning or anything operational — the cadence is six-monthly"
  - "Spatial analysis without first sourcing the sensor coordinates elsewhere"
  - "Using `valore` without filtering on `stato`"
---

## What it is

Every rainfall reading from ARPA Lombardia's hydro-nivo-meteorological monitoring network since 1
January 2021, at the finest resolution available — down to ten-minute steps. **67,262,315 rows.**
Four columns: sensor id, value, timestamp, status.

This is the largest dataset on the site by a wide margin, and for climate and hydrology work at
regional scale it is a serious resource. Ten-minute rainfall over five years across an entire
Italian region, in the public domain, is not a common thing to be able to download.

## How it holds up

**The substance and the licence are both excellent.** The temporal resolution is what makes extreme
rainfall analysis possible at all — hourly totals hide the short intense bursts that cause urban
flooding. Five years is enough for meaningful statistics and it keeps accumulating. CC0 means no
attribution obligation and no negotiation.

The cadence declaration is honest and kept: `semestrale`, six-monthly, and the file was 157 days old
when we measured it, comfortably inside that window. On a portal where
[27.6% of promises are kept](/evaluations/dati-lombardia/), this one is.

**And then the file does not say where anything happened.** The four columns are `idsensore`,
`valore`, `data`, `stato`. The sensor is an integer — `8199` in the first row we pulled. There is no
latitude, no longitude, no station name, no municipality, and no link from this dataset to a registry
that would supply them.

Normalising station metadata out of a 67-million-row observation table is defensible engineering;
repeating coordinates 67 million times would be wasteful. What is not defensible is failing to point
at the other half. A user who wants to know whether it rained in Bergamo cannot answer that question
from this dataset, and nothing on the page tells them where to look. The join exists — ARPA publishes
a sensor registry — but finding it is left as an exercise.

**`stato` is the second gap.** All four columns are technically documented, but the documentation
does not enumerate the status vocabulary. We observed `VA`, presumably *validato*. Whether other
codes indicate provisional, suspect or invalid readings, and which of them should be excluded from a
total, is not stated. On a sensor series this is the difference between a rainfall total and a
rainfall total plus some instrument errors.

**Accessibility scores slightly below the portal norm** for a practical reason: 67 million rows over
SODA means paging, and a naive request will not return the series. It is still ungated and fast per
page.

## Working with it

Find the ARPA station registry first and build the sensor-to-location lookup before anything else;
without it the data is a time series of anonymous integers.

Filter on `stato` and state which codes you kept. Page the API with `$limit` and `$offset`, or take
the bulk export if you need the whole series — 67 million rows is not an interactive query.

For sub-hourly work, check the actual step per sensor. The description says up to ten minutes, which
implies it varies.

## The call

**Grade B.** The data is outstanding, the resolution is genuinely valuable, the licence is the best
available and the publisher keeps the cadence it declares. Two omissions hold it a grade below where
it should be, and both are links rather than work: a pointer to the station registry, and a table of
what `stato` means.
