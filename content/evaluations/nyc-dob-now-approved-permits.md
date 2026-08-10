---
title: "DOB NOW: Build — Approved Permits"
date: 2026-08-10
publishers: ["NYC Department of Buildings"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Housing", "Governance"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/rbx6-tga4"
version: "Rolling feed — 981,823 rows at snapshot"
snapshot: 2026-08-10
temporal: "2016 to present"
updated: "9 August 2026"
cadence: "Declares Daily, automated, and keeps it"
formats: ["CSV", "JSON", "GeoJSON", "RDF", "TSV"]
size: "981,823 rows, 46 columns"
access: "Open API and bulk download, no registration"

verdict: "The system that replaced a fully documented dataset, documenting nothing."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 9
  documentation: 2
  accessibility: 9
  licensing: 3
  interoperability: 6

strengths:
  - "Genuinely current: declared Daily, automated, and updated the day before we pulled it."
  - "Latitude and longitude ship as their own numeric columns alongside BIN and BBL, so it maps and joins without geocoding."
  - "981,823 permits with owner, applicant, filing representative and work type — a detailed picture of who is building what."
weaknesses:
  - "**Not one of its 46 columns carries a description**, while the legacy dataset it replaced documents all 95 of its own."
  - "It covers approved permits only, and excludes electrical, elevator and plumbing, each of which lives in a separate dataset. The name does not say so."
  - "`job_filing_number` and `work_permit` occasionally contain the sentence `Permit is not yet issued` instead of an identifier — rare (2 rows in 2,000) but enough to break a naive cast."

bestfor:
  - "Current New York construction permitting, as the live half of the DOB series"
  - "Mapping approved work — coordinates are already there"
avoidfor:
  - "Any complete picture of permits without also pulling the electrical, elevator and plumbing feeds"
  - "Assuming identifier columns are always identifiers"
---

## What it is

Approved construction permits from DOB NOW, the New York City Department of Buildings' current
filing platform: 981,823 rows, 46 columns, updated daily since 2016. It is the live continuation of
the story that [DOB Job Application Filings](/evaluations/nyc-dob-job-application-filings/) tells up
to the migration.

## How it holds up

**The engineering is fine and the timeliness is genuinely good.** Daily, automated, current. Latitude
and longitude arrive as numeric columns, and `bin`, `bbl`, `c_b_no` and council district are all
present, so this maps and joins with no preparation. For a live permitting feed that is what matters
most and the department delivers it.

**The documentation is the story, and it is a striking one.** Zero of 46 columns carry a
description.

That number would be unremarkable on this portal — 31.1% column coverage is the site-wide average —
except for what sits next to it. The same agency's legacy filings dataset documents **all 95** of its
columns. Same department, same portal, same publishing pipeline, and the new system that replaced
the old one dropped the practice entirely.

So a user who moves from the legacy dataset to the current one, which is exactly the journey the
migration forces on them, goes from a fully documented file to an undocumented one. Fields like
`filing_reason`, `work_type`, `permittee_s_license_type` and `sequence_number` are guessable by an
expert and opaque to everyone else.

**Scope is the second gap.** The title says Approved Permits. The description then explains that
electrical, elevator, plumbing and several other permit types are excluded and live in their own
datasets. Anyone summing permits from this file alone will undercount, and the shortfall is
structural rather than random.

**One data defect worth naming precisely, because we nearly overstated it.** In a 3-row preview,
`job_filing_number` and `work_permit` both read `Permit is not yet issued` — a sentence in an
identifier column. Pulling 2,000 rows put it in proportion: 1,847 distinct filing numbers, and the
sentinel appears twice, about 0.1%. It is not endemic. It is still a string in a column that a
consumer will reasonably treat as a key, and it will break a cast the first time it appears.

## Working with it

Pull the sibling permit datasets — electrical, elevator, plumbing — if you need permitting totals.
Filter or coerce the identifier columns before casting. Use `permit_status`, which is clean: in our
sample it takes exactly two values, `Permit Issued` and `Signed-off`.

For the fields you cannot interpret, the legacy dataset's dictionary is the closest thing to a
codebook, since many columns are conceptual descendants of documented ones.

## The call

**Grade B−.** Live, mappable, richly detailed and completely unexplained. The documentation score of
2 is not a resourcing problem — the same team documented 95 columns on the previous system. Copying
that practice forward would take this to a solid B and cost nobody anything they have not already
done once.
