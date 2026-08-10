---
title: "NYCgov Poverty Measure (2017)"
date: 2026-08-10
publishers: ["NYC Mayor's Office for Economic Opportunity"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Population", "Society"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/76hw-72td"
version: "2017 edition — 68,094 records, published July 2021"
snapshot: 2026-08-10
temporal: "Survey year 2017"
updated: "27 July 2021"
cadence: "Declares Historical data — a closed edition, correctly marked"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "68,094 person records, 61 columns"
access: "Open API and bulk download, no registration"

verdict: "A serious alternative poverty measure, shipped as sixty-one ACS variable codes and no codebook."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 4
  documentation: 2
  accessibility: 9
  licensing: 3
  interoperability: 7

strengths:
  - "Person-level microdata with survey weights (`pwgtp`, `wgtp`) intact, so properly weighted estimates and standard errors are possible."
  - "Carries the city's own constructed measures alongside the federal ones — `est_povgap`, `off_threshold`, `nycgov_rel`, `est_eitc`, `est_childcare`, `est_moop`."
  - "Honestly declared `Historical data`: a closed edition, not a live series left to look current."
weaknesses:
  - "**Zero of 61 columns documented**, on a file whose column names are raw ACS PUMS abbreviations — `esr`, `jwtr`, `ten`, `mar`, `agep`, `cit`."
  - "The description is one sentence: *American Community Survey Public Use Micro Sample, augmented by NYC Opportunity.* The augmentation is the entire point and is not explained here."
  - "The 2017 edition was published in July 2021 and is the copy on the portal, so the most recent NYC poverty measure on open data describes conditions nine years before this review."

bestfor:
  - "Replicating New York's alternative poverty measure, if you already know ACS PUMS"
  - "Comparing the city measure against the official federal threshold on the same records"
avoidfor:
  - "Current poverty estimates for New York"
  - "Anyone without the ACS PUMS data dictionary open beside them"
---

## What it is

New York City's alternative poverty measure: 68,094 person records drawn from the American Community
Survey Public Use Microdata Sample for 2017, augmented by the Mayor's Office for Economic
Opportunity with the city's own threshold, its own income definition, and estimates of the transfers
and expenses the official federal measure ignores.

This is a substantively important product. The federal poverty threshold is widely held to
misdescribe a high-cost city, and NYC's measure is one of the more serious municipal attempts to fix
that — accounting for housing costs, tax credits, nutrition assistance and out-of-pocket medical
spending. The columns bear that out: `est_eitc`, `est_nutrition`, `est_moop`, `est_incometax`,
`est_povgap`, `off_threshold`.

## How it holds up

**As microdata it is properly built.** Person and household weights survive as `pwgtp` and `wgtp`,
which means weighted estimates and replicate-based standard errors are achievable. `serialno` and
`sporder` preserve the household structure. Nothing about the file's construction is wrong.

**As a publication it is close to unusable without external help.** Zero of 61 columns carry a
description, and the column names are not English — they are ACS PUMS mnemonics. `esr` is employment
status recode. `jwtr` is means of transportation to work. `ten` is housing tenure. `mar` is marital
status. `cit` is citizenship. A reader who does not already have the Census Bureau's PUMS data
dictionary cannot interpret a single one of them, and the dataset does not link to it.

The city-constructed variables are worse off, because no external dictionary covers them. `nycgov_rel`,
`est_povgap` and `off_threshold` exist only in this methodology. Their definitions live in the Mayor's
Office annual poverty report, which is not referenced from the dataset page. The entire distinctive
contribution of the file — the augmentation — is the part with no documentation anywhere near it.

The whole description reads: *American Community Survey Public Use Micro Sample, augmented by NYC
Opportunity.* Thirteen words for a 61-variable methodological product.

**On timeliness it is honest but old.** It declares `Historical data`, which is the correct label for
a closed annual edition and we credit it. But the 2017 edition was published in July 2021, and it is
what the portal offers. Poverty measurement is only useful in series, and a reader arriving today
finds a nine-year-old snapshot.

## Working with it

Open the Census Bureau's ACS PUMS data dictionary for 2017 before you open the file; roughly
two thirds of the columns are documented there. For the `est_*` and `nycgov_*` fields, find the
Mayor's Office poverty report for the same year — that is where the definitions are.

Apply the weights. Unweighted counts from PUMS are not estimates of anything.

## The call

**Grade C+.** The methodology is serious and the microdata is correctly constructed, which is why
completeness and interoperability score reasonably. What drags it to a C+ is that a specialist
product with 61 coded variables has been published with no codebook, no link to one, and a
thirteen-word description — and then left at 2017.

A link to the ACS dictionary and a table of the city's own derived fields would be an afternoon's
work and would move this several grades. The analysis exists; it is in a PDF somewhere, not attached
to the data.
