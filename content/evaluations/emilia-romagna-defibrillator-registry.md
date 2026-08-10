---
title: "Emilia-Romagna Defibrillator Registry"
date: 2026-07-30
publishers: ["Comune di Bologna"]
regions: ["Europe"]
places: ["Bologna"]
domains: ["Health", "Geospatial"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/progetto-dae/"
temporal: "Current register, no history"
updated: "Same day"
cadence: "Declares WEEKLY, and beats it"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX"]
size: "6,197 defibrillators across Emilia-Romagna"
access: "Direct download and API, no registration"

verdict: "A register of life-saving equipment where half the entries do not say when you can reach it and the phone column is empty in every single row."
reviewer: "Ministry desk"

scores:
  completeness: 5
  timeliness: 9
  documentation: 2
  accessibility: 9
  licensing: 9
  interoperability: 4

strengths:
  - "Every record is geolocated, and the geometry is clean — 1,991 distinct coordinates across 2,000 sampled rows."
  - "Declares WEEKLY and updates daily. For a register that determines whether a device is where it says it is, that matters."
  - "Openly licensed with no registration, which is the correct decision for emergency infrastructure."
weaknesses:
  - "**`telefono` is empty in 100% of records.** A contact column is published on an emergency dataset and it contains nothing at all."
  - "`orari` — when the device is accessible — is empty in 49.8% of records, and where present it is a Python dict repr in a text field, single-quoted and not parseable as JSON."
  - "None of the 11 fields carries a description, and the dataset is regional despite sitting on Bologna's municipal portal — the most common `quartiere` value is `FUORI BOLOGNA`."

bestfor:
  - "Mapping AED locations across Emilia-Romagna"
  - "Coverage-gap analysis against population or incident data"
  - "Prompting a conversation with the publisher about the empty columns"
avoidfor:
  - "Any application that tells a member of the public a defibrillator is available right now"
  - "Assuming a Bologna-only extract — most rows are elsewhere in the region"
  - "Parsing `orari` with a JSON reader"
---

## What it is

The Registro Regionale Unico dei Defibrillatori: 6,197 automated external defibrillators across
Emilia-Romagna, each with a name, address, city, a description of where in the building it sits,
opening hours, notes, and a coordinate. It is published on Bologna's municipal portal but its scope
is the whole region — the top values in `citta` are Ferrara, Reggio nell'Emilia and Modena, and the
single most common value of `quartiere` is `FUORI BOLOGNA`.

This is, in principle, one of the most directly useful datasets a public body can publish. In a
cardiac arrest, minutes decide outcomes, and knowing where the nearest AED is and whether you can
physically get to it is the entire point of maintaining a register.

## How it holds up

**The plumbing is good.** It updates daily against a declared weekly cadence, every record is
geolocated to five or six decimal places, and it is openly licensed with no gate. Somebody has built
this properly.

**The contents are where it falls apart, and the specifics are difficult to defend.**

`telefono` is empty in **every single record** we sampled — 100%, 2,000 out of 2,000. A phone number
column exists in the schema of an emergency dataset and carries no data whatsoever. It should either
be populated or removed; publishing an empty column implies information that is not there.

`orari` — the hours during which the device can actually be reached — is **empty in 49.8% of
records**. For half the register, the dataset locates a defibrillator and says nothing about whether
you could get to it at three in the morning. Given that `ubicazione` values include `TECA ESTERNA`
(external cabinet), `RECEPTION` and `INFERMERIA`, accessibility varies enormously and the field that
would tell you is a coin flip.

Where `orari` is populated, it arrives like this:

```
{'LUNEDI': '08:00-17:00', 'MARTEDI': '08:00-17:00', ...}
```

That is a Python dictionary's `repr` written into a text column. Single quotes, so it is not JSON
and `json.loads` fails on it. Anyone consuming this either writes an `ast.literal_eval` and accepts
the security posture that implies, or writes a regex. Neither should be necessary to find out when a
defibrillator is available.

**Not one of the 11 fields is documented.** On a dataset where `note` contains free text like
*"Disponibilità non programmata"* — availability not guaranteed — and appears in 28.2% of records,
the absence of any statement about how `note`, `orari` and `ubicazione` interact is a genuine
obstacle to using this safely.

## Working with it

Treat `orari` as unreliable and `telefono` as absent. Filter on `citta` if you want Bologna; the
municipal fields are populated with `FUORI BOLOGNA` for the majority of the region.

If you are building anything public-facing, do not present a device as available without a caveat.
The honest rendering of this data is "an AED is registered at this location", not "an AED is
available here now" — and the dataset cannot support the second claim for half its rows.

## The call

**Grade B−**, and it is the lowest documentation score we have awarded to a dataset that is
otherwise well run. The engineering, licensing and refresh cadence are all fine. What is missing is
the content of two columns and eleven sentences of documentation.

The gap between this and a genuinely excellent dataset is small and entirely clerical. Given what it
is a register of, it is also the gap that matters most.
