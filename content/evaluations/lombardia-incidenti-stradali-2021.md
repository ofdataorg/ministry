---
title: "Incidenti Stradali — Microdati 2021"
date: 2026-08-10
publishers: ["Regione Lombardia", "ISTAT"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Mobility", "Health"]
licenses: ["CC BY 4.0"]

source: "https://www.dati.lombardia.it/d/siha-gvxr"
version: "2021 edition — 25,838 records, published January 2025"
snapshot: 2026-08-10
temporal: "Calendar year 2021"
updated: "20 January 2025"
cadence: "Declares Mai (never) — correct for a closed annual file"
formats: ["CSV", "JSON", "GeoJSON", "RDF", "TSV"]
size: "25,838 records, 22 columns"
access: "Open API and bulk download, no registration"

verdict: "Every injury collision in Lombardia for a year, at incident level, with none of the codes explained."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 4
  documentation: 2
  accessibility: 9
  licensing: 8
  interoperability: 6

strengths:
  - "Incident-level microdata, not aggregates: 25,838 collisions with municipality, month, road type, vehicle types and driver ages."
  - "It carries both ISTAT mortality conventions — deaths within 24 hours and deaths within 30 days — as separate columns, which is the distinction international comparison turns on."
  - "CC BY 4.0, no registration, and it joins to any Italian dataset through `codice_istat_comune`."
weaknesses:
  - "**Zero of 22 columns documented**, on a file built almost entirely from ISTAT numeric codes. `localizzazione_incidente` is published as `5`, and nothing says what 5 means."
  - "Collisions from 2021 were published in January 2025 — a lag of roughly three years on casualty statistics."
  - "Driver fields are suffixed `_a`, `_b`, `_c` for the vehicles involved, with no statement of ordering, so a two-vehicle collision's `_c` columns are silently empty rather than absent."

bestfor:
  - "Road safety analysis at municipality level for Lombardia"
  - "Work needing the 24-hour versus 30-day death distinction"
  - "Joining collision counts to population or road network data"
avoidfor:
  - "Current road safety monitoring"
  - "Interpreting any coded field without the ISTAT survey codebook"
---

## What it is

The microdata behind ISTAT's national survey of road collisions involving personal injury
(IST-00142), for Lombardia in 2021: 25,838 records, one per collision, with the municipality, the
month, the road and its type, the vehicles involved, the ages of their drivers, and the casualties.

Incident-level collision microdata is a genuinely valuable thing for a region to publish. Most
authorities release counts by year and province; this lets you ask about a specific junction, a
specific vehicle pairing, a specific age band.

## How it holds up

**On substance it is strong.** The record structure is right, `codice_istat_comune` makes it joinable
to every other Italian dataset, and — the detail that shows somebody understood the domain — it
carries `tot_morti_a_24ore_incidente` and `tot_morti_a_30gg_incidente` as separate columns.

That distinction matters more than it looks. Road deaths are internationally reported on a 30-day
definition; Italy historically collected 24-hour figures, and the two differ by several percent.
Publishing both means the data can be reconciled with European statistics rather than quietly
diverging from them. Keeping it was the correct call.

**On documentation it is at the floor.** Zero of 22 columns carry a description, and this is a file
made of codes. `localizzazione_incidente` arrives as `5`. `natura_incidente` is a number.
`tipo_strada` is a number. `tipo_veicolo_a`, `_b` and `_c` are numbers. Every one of them maps to an
ISTAT classification, and none of the mappings are here or linked from here.

The consequence is concrete: a reader can count collisions but cannot say what kind they were. The
codebook exists — it is the ISTAT survey documentation — and connecting the two is a hyperlink that
nobody added.

The `_a`/`_b`/`_c` suffixing is the second trap. Vehicles are enumerated up to three, so a
single-vehicle collision leaves the `_b` and `_c` fields empty. That is correct behaviour and
indistinguishable, without documentation, from a missing value.

**On timeliness the label is right and the lag is not.** It declares `Mai` — never updated — which
is exactly correct for a closed annual file, and we credit the honesty. But the 2021 collisions were
published in January 2025. Road safety data three years after the fact is a research resource, not
an input to road safety policy.

## Working with it

Fetch the ISTAT IST-00142 documentation and build the code lookups before analysis; nothing here is
interpretable without them. Treat empty `_b`/`_c` columns as "no such vehicle", not as missing data.

Use the 30-day death column for anything compared internationally, and say which you used.

## The call

**Grade B−.** The underlying survey is rigorous, the record structure is right, the licence is clean
and the mortality conventions are handled properly. It is held down by a complete absence of
documentation on a file that is almost entirely coded, and by a three-year publication lag on data
whose main value would be timely.

One link to the ISTAT codebook would move the documentation score more than any other single change
available to this publisher.
