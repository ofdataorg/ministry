---
title: "Bologna Parking Sensors — Trento e Trieste"
date: 2026-07-29
publishers: ["Comune di Bologna"]
regions: ["Europe"]
domains: ["Mobility"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/parcheggi_dati_trento_trieste/"
temporal: "Rolling history to the current hour"
updated: "Same day, every day"
cadence: "Declares DAILY via dcat:accrualPeriodicity, and beats it"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX", "SHP"]
size: "1,544,113 records from 7 sensors"
access: "Direct download and API, no registration"

verdict: "The freshest dataset in the whole Bologna catalogue and the least explained — eight columns, not one of them documented."
reviewer: "Ministry desk"

corrections:
  - date: 2026-07-30
    text: "The spec sheet originally said the update cadence was not stated in the metadata. Wrong — this dataset declares DAILY via `dcat:accrualPeriodicity`, as do all 702 in the catalogue. We had checked only the portal's native field. The timeliness score of 10 is unchanged; it beats its own declaration."

scores:
  completeness: 5
  timeliness: 10
  documentation: 2
  accessibility: 9
  licensing: 9
  interoperability: 5

strengths:
  - "Genuinely live. Records were current to within hours of us pulling it, with no gap between the sensor and the public file."
  - "1.5 million observations from a fixed sensor array — dense enough for real occupancy modelling at a single junction."
  - "CC BY 4.0, no registration, and Parquet and GeoJSON exports available alongside CSV."
weaknesses:
  - "**Zero of eight fields carry a description.** A column named `detectedobjects` is published with no statement of what object is being detected."
  - "`online` reads `True` in every record we sampled, so sensor downtime is invisible — a gap in the data and a genuinely empty parking bay are indistinguishable."
  - "Three time columns in two conventions: `createdat` and `updatedat` in ISO 8601, `timestamp` as a Unix epoch, with nothing saying which is authoritative."

bestfor:
  - "Occupancy and turnover analysis at one Bologna junction"
  - "Testing streaming or near-real-time pipelines against a live public feed"
  - "A worked example of how far good plumbing gets you without a data dictionary"
avoidfor:
  - "Any claim about parking availability across Bologna — this is seven sensors"
  - "Treating an absent record as a free space"
  - "Analysis that needs to distinguish sensor failure from genuine vacancy"
---

## What it is

A live feed from seven parking sensors around Piazza Trento e Trieste in Bologna, published as a
rolling history of 1,544,113 records. Each row is one sensor reporting at one moment: a device
identifier, a coordinate, a count of detected objects, a status, and three timestamps.

It is the freshest thing in the [Bologna catalogue](/evaluations/comune-di-bologna-open-data/) —
when we pulled it, the most recent record was hours old — and it is a good illustration of what that
portal does well. The plumbing is excellent. Everything downstream of the plumbing is missing.

## How it holds up

**On timeliness it is a straight ten and we are happy to give it.** There is no publication lag
worth measuring. The sensor reports, the record appears, anyone can have it. For a municipal feed
that is genuinely good engineering. The dataset declares DAILY through `dcat:accrualPeriodicity` and
comfortably beats its own promise.

**On documentation it is close to the floor.** Eight fields. Zero descriptions. The dataset page
carries a 931-character narrative description and not one line explaining what a column contains.

Consider `detectedobjects`, which takes integer values from 0 to about 10. Detected objects of what
kind? Cars? People? Bicycles? Any moving thing in the sensor's cone? The answer determines whether
this dataset measures parking occupancy or pedestrian traffic, and the file does not say. We can
infer it is vehicles from the dataset's title and nothing else, which is not the same as knowing.

Then `status`, which takes `BUSY` and `FREE`. Across a 3,000-record sample it is **100% redundant**:
every `FREE` is a row where `detectedobjects` is 0, every `BUSY` is a row where it is not, with zero
mismatches. It is a derived column shipped as if it were an observation. Harmless once you know;
misleading if you assume it is an independent signal from the sensor.

And `online`, which reads `True` in every record we sampled. A field that never varies is either
broken or it means the file only contains rows from working sensors — in which case **downtime is
invisible**. There is no way to tell a period when a bay was empty from a period when the sensor was
dead. For an occupancy time series that is the single most consequential thing a user needs to know,
and it is not knowable from the data.

The device identifiers are opaque UUIDs like `81598086-a0f7-4cf0-aab9-16b564c4783b`, each pinned to
one fixed coordinate. There is no lookup table mapping a sensor to a human-readable location, so
identifying which bay is which means reverse-geocoding the coordinates yourself.

**Completeness scores mid.** Within its scope the record density is excellent. But the scope is
seven sensors at one junction, the title does not make that obvious, and — because of the `online`
problem — the gaps are not legible. Our completeness axis rewards datasets that document where they
are thin. This one cannot.

## Working with it

Pull Parquet or GeoJSON rather than CSV. If you must take CSV, it arrives semicolon-delimited with a
UTF-8 BOM, so read it with `delimiter=';'` and `encoding='utf-8-sig'` or your first column will be
called `﻿createdat` and your frame will have one column.

The `coordinate` field is a single string — `"44.4877802641266, 11.360635505726904"` — rather than
two numeric columns, so split and cast it before any spatial work. Pick one time column and stay
with it; `timestamp` is a Unix epoch while `createdat` and `updatedat` are ISO 8601 with an offset,
and mixing them silently is easy.

Drop `status` and derive occupancy from `detectedobjects` yourself. You will get the identical
answer and you will know how you got it.

Most importantly: do not treat absence of a record as a free space. Until the publisher explains
what `online` is for, an absent row means "no information", and any occupancy rate you compute
should carry that caveat explicitly.

## The call

**Grade B**, and the spread inside it is the story. Timeliness 10, documentation 2. This is a
dataset that solves the genuinely hard problem — getting a sensor's output in front of the public
in near-real time, under an open licence, with no gate — and then declines to spend an hour writing
eight sentences that would make it trustworthy.

Eight field descriptions and a note on what `online` means would take one person one afternoon and
would move this from a curiosity to a dataset you could publish research on. The engineering is
already done. It is the last mile that is missing, and it is the cheap mile.
