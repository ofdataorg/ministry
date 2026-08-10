---
title: "DOB Job Application Filings"
date: 2026-08-10
publishers: ["NYC Department of Buildings"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Housing", "Governance"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/ic3t-wcy2"
version: "Rolling feed — 2,715,897 rows at snapshot"
snapshot: 2026-08-10
temporal: "Latest action date from January 2000"
updated: "9 August 2026"
cadence: "Declares Daily, automated, and keeps it"
formats: ["CSV", "JSON", "GeoJSON", "RDF", "TSV"]
size: "2,715,897 rows, 95 columns"
access: "Open API and bulk download, no registration"

verdict: "Ninety-five columns, every one documented — describing a system New York stopped filing most new work in a decade ago."
reviewer: "Ministry desk"

scores:
  completeness: 5
  timeliness: 9
  documentation: 8
  accessibility: 9
  licensing: 3
  interoperability: 7

strengths:
  - "**All 95 columns carry a description.** Full documentation on a 95-column dataset is rare anywhere and we have not seen it elsewhere in this catalogue."
  - "Daily, automated, and current — it had updated the day before we pulled it, against a declared Daily cadence."
  - "Rich joinable identifiers: BBL, BIN, census tract, community board and council district all present, so it links to the rest of the city's data without geocoding."
weaknesses:
  - "**It excludes everything filed through DOB NOW**, the system the Department of Buildings has been migrating to since 2016. The most-consulted construction dataset in New York is a partial view."
  - "The exclusion is stated once, in prose, in the dataset description. Nothing in the data marks where coverage stops."
  - "No licence, in common with 97.4% of the [portal](/evaluations/nyc-open-data/)."

bestfor:
  - "Construction filing history from 2000 up to the DOB NOW migration"
  - "Property-level joins via BBL or BIN"
  - "A model of what full column documentation looks like"
avoidfor:
  - "Any claim about current construction activity in New York without also pulling the DOB NOW datasets"
  - "Counting filings over time across the migration boundary"
---

## What it is

Every job application filed with the New York City Department of Buildings through the borough
offices, eFiling or the HUB, with a latest action date since January 2000. 2,715,897 rows and 95
columns, updated daily by an automated pipeline, and the third most-viewed dataset the city
publishes — 2.4 million page views.

## How it holds up

**The documentation is the best we have measured.** All 95 columns carry a description. On a file
with fields like `existing_zoning_sqft`, `site_fill`, `doc__` and `special_action_date`, that is the
difference between a usable dataset and a guessing game, and the Department of Buildings has done it
in full. Set against the same agency's newer [DOB NOW permits
feed](/evaluations/nyc-dob-now-approved-permits/), which documents none of its 46 columns, it shows
this was a choice rather than a capability.

Timeliness is equally good: declared Daily, flagged as automated, and updated the day before we
pulled it.

**And then the scope, which is the problem.** The description opens by saying the dataset contains
job applications filed through the borough offices, eFiling or the HUB — and then adds, in one
sentence, that *it does not include jobs submitted through DOB NOW*.

DOB NOW is the department's replacement filing system, rolled out progressively from 2016. Which
means this dataset — the one a search for New York construction filings lands on, the one with 2.4
million views — captures the legacy system and stops. New work increasingly appears somewhere else,
in a family of separate DOB NOW datasets split by permit type.

Nothing in the data itself marks this. There is no coverage flag, no end-date field, no column
saying "filings after this point are elsewhere". A user who plots filings per year from this file
alone will see construction in New York apparently collapse, and the collapse is an artefact of a
software migration.

That is a completeness failure of the specific kind our rubric cares about most: the gap is real,
consequential, and not legible from the data. It costs the score heavily despite everything else
being done well.

## Working with it

Pull the DOB NOW datasets alongside this one and treat the pair as a single logical series with a
seam in it. Expect the seam to be gradual rather than a clean cutover, because the migration was
phased by permit type.

Use `bbl` for property joins. Watch the identifier columns: `job__` and `job_s1_no` are different
things and the trailing-underscore naming is Socrata sanitising a `#`.

## The call

**Grade B.** On craft this is among the best-run datasets in the catalogue — fully documented, truly
daily, richly joinable. It is held back by a scope boundary that matters enormously and is mentioned
once in prose.

One column recording which filing system a row came from, and a line in the description saying where
the series continues, would fix the most consequential thing about it. The documentation discipline
to do that is demonstrably already there.
