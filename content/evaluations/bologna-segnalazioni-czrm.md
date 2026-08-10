---
title: "Bologna Citizen Reports (CZRM)"
date: 2026-07-30
publishers: ["Comune di Bologna — Dipartimento Cura e Qualità del Territorio"]
regions: ["Europe"]
places: ["Bologna"]
domains: ["Governance", "Society"]
licenses: ["CC BY 4.0"]

source: "https://opendata.comune.bologna.it/explore/dataset/segnalazioni-open-citizen-relationship-management-czrm/"
temporal: "Rolling history of citizen reports"
updated: "July 2026"
cadence: "Declares MONTHLY, and meets it"
formats: ["CSV", "JSON", "GeoJSON", "Parquet", "XLSX"]
size: "123,823 reports"
access: "Direct download and API, no registration"

verdict: "What 123,000 residents complained about, where, and in what order of category — with no record of whether anyone ever fixed it."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 8
  documentation: 6
  accessibility: 9
  licensing: 9
  interoperability: 6

strengths:
  - "A three-level category hierarchy — degrado urbano, viabilità, verde pubblico and 14 top-level types down to 91 leaf categories — makes this genuinely analysable rather than a pile of free text."
  - "Every report is geolocated and carries quartiere, statistical area and proximity zone, so it joins straight to census geography."
  - "No free-text complaint bodies, so it is publishable without a privacy fight. Somebody thought about disclosure before releasing it."
weaknesses:
  - "**There is no outcome field.** You can see what was reported and never whether it was resolved, refused, or ignored, which is the question the data invites."
  - "Coordinates ship three times per row — `geopoint`, plus `latitude` and `longitude` as *text* columns — which is redundant and mistyped at once."
  - "The category hierarchy is sparse below the first level: `sottocategoria_02` is empty in 13.1% of rows and `sottocategoria_03` in 26.1%, with no stated rule for when a level applies."

bestfor:
  - "Mapping the geography of urban maintenance complaints"
  - "Joining reported problems to demographic or deprivation data by statistical area"
  - "Studying reporting behaviour — who complains, about what, and from where"
avoidfor:
  - "Any claim about council responsiveness or resolution rates"
  - "Reading report density as problem density rather than reporting propensity"
  - "Assuming the three subcategory levels form a complete tree"
---

## What it is

Every report submitted to Bologna's citizen relationship management system: 123,823 records, each
with a timestamp, a location, a district, a statistical area, a proximity zone, and a three-level
category. Reports split into `Segnalazioni` (problems), `Richieste di informazioni` (information
requests) and `Suggerimenti` (suggestions).

The categories are the interesting part. Fourteen top-level types — urban decay, roads and traffic,
public greenery — branching to 72 second-level and 91 third-level values covering things like
`Rifiuti/rottami`, `Veicoli abbandonati/carcasse di veicoli` and `Dissestate`. This is a structured
picture of what a city's residents find wrong with it, at street resolution, over years.

## How it holds up

**The disclosure thinking is good and should be credited.** There are no free-text complaint bodies
and no reporter identifiers. Somebody worked out that publishing what people wrote would be a
privacy problem and published the structure instead. A great many authorities either dump the lot or
publish nothing; this is the correct middle path.

**The geography is genuinely useful.** `codice_area_statistica` and `nome_area_statistica` join
directly to Bologna's statistical geography, which means these reports can be normalised by
population, cross-referenced with deprivation, or compared across districts without any geocoding
work. That is what turns a complaints log into research material.

**And then there is no outcome.** Not one field records what happened. Was the abandoned vehicle
removed? Was the pothole filled, and how long did it take? Was the report closed as a duplicate, or
refused, or simply left open?

This is the single most consequential absence in the dataset, because it defines what can be asked
of it. A CRM system by definition tracks status — reports are opened, assigned, worked and closed —
so the information exists inside the municipality. What has been published is the half that makes
residents visible and the administration invisible. You can study what Bologna's citizens complain
about; you cannot study what Bologna does about it. For an open government dataset, that asymmetry
is worth naming plainly.

**The schema has a redundancy problem** familiar from elsewhere on this portal. Every row carries
`geopoint` as a proper geo type *and* `latitude` and `longitude` as separate columns — declared as
`text`, not numeric. Three representations of one fact, one of them wrongly typed.

**Documentation is middling**: 7 of 13 fields described. The undocumented ones include the
subcategory columns, which is where a user most needs guidance — nothing states when a report gets
two levels rather than three, so the 13.1% and 26.1% empty rates could mean "not applicable" or
"not recorded" and there is no way to tell.

## Working with it

Normalise by population before comparing districts. Raw report counts measure reporting propensity
at least as much as they measure problems, and propensity correlates with age, tenure, language and
confidence in the council — the same variables you are probably trying to study.

Use `geopoint`, ignore the text lat/long columns. Treat missing subcategory levels as unknown rather
than as a category.

## The call

**Grade B+.** Well-structured, well-geocoded, sensibly anonymised and released on a cadence it
actually keeps — as a picture of civic demand this is a strong dataset and better than most cities
publish.

The score reflects what is missing rather than what is wrong. Add a status and a resolution date and
this becomes something considerably more valuable and considerably more uncomfortable: a public
record of whether the city answers its residents. The data already exists in the system that
generated this file.
