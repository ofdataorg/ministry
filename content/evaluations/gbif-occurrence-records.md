---
title: "GBIF Occurrence Records"
date: 2026-07-11
publishers: ["Global Biodiversity Information Facility"]
regions: ["Global"]
place: "Global"
places: ["Global"]
domains: ["Biodiversity", "Science"]
licenses: ["CC0 / CC BY / CC BY-NC (mixed)"]

source: "https://www.gbif.org/occurrence/search"
temporal: "18th century specimens to yesterday's bird sighting"
updated: "Continuously"
cadence: "Rolling — publishers push, index refreshes daily"
formats: ["Darwin Core Archive", "CSV", "Parquet"]
size: "Billions of occurrence records from thousands of publishers"
access: "Free; account required to trigger a download, DOI minted per query"
verdict: "The most impressive aggregation infrastructure in open science, sitting on top of the most biased sample in it."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 9
  documentation: 9
  accessibility: 9
  licensing: 7
  interoperability: 9

strengths:
  - "Every download gets a DOI with the exact query and the contributing dataset list attached. Reproducibility is the default, not a virtue you have to practise."
  - "Darwin Core is a real standard, properly applied, with interpretation flags exposed rather than hidden."
  - "The API is generous, well documented, and stable enough to build on."
weaknesses:
  - "Sampling effort is wildly uneven — by continent, by taxon, by decade. Absence of records is almost never absence of species."
  - "Per-record licences are mixed; a single download can contain CC0, CC BY and CC BY-NC rows that you must then honour separately."
  - "Coordinate quality varies from survey-grade to centroid-of-country. The flags tell you, but only if you read them."

bestfor:
  - "Species distribution modelling, with effort correction"
  - "Finding which institution holds a specimen"
  - "Reproducible, citable extracts for a paper"
avoidfor:
  - "Naive abundance or trend estimates"
  - "Inferring that a species is absent somewhere"
  - "Bulk commercial reuse without a licence audit"
---

## What it is

GBIF is not a dataset, it is an index. Thousands of museums, herbaria, national agencies and citizen
science platforms publish occurrence records — a taxon, a place, a time, a basis of record — and
GBIF harmonises them into Darwin Core and makes the whole thing searchable and downloadable. The
result is the largest single window onto where life has been observed.

The engineering deserves the praise it gets. You construct a query, you get a DOI, and that DOI
resolves to the exact constituent datasets and record counts that made up your download. Anyone can
re-derive your extract years later. Most of open science still cannot do this.

## How it holds up

The infrastructure scores near the top on every axis we measure. The problem is not GBIF's, and GBIF
is admirably direct about it: the underlying sample is a record of *observers*, not of *nature*.

Northern Europe and North America are covered orders of magnitude more densely than the tropics that
hold most of the biodiversity. Birds dominate because eBird dominates. Records cluster along roads,
around research stations, and on weekends. Digitisation backlogs mean a herbarium's nineteenth
century holdings may appear as a step change in 2013 with no ecological meaning whatsoever.

None of that makes the data bad. It makes unweighted analysis of it wrong. Every credible use of
GBIF at scale involves an effort-correction step, and the ones that skip it produce maps of where
biologists live.

The licensing is the one genuinely awkward technical detail. Records carry the licence their
publisher chose, so a mixed download inherits the strictest term in it. If any of your rows are
CC BY-NC, your derived product is constrained by that, and the constraint travels with you into
whatever you build. Check the composition before you promise anyone a commercial deliverable.

## Working with it

Use the API for exploration and the download service for anything you will cite. Take the Parquet
export over CSV for anything large. Read the `issue` flags — `COUNTRY_COORDINATE_MISMATCH` and the
various rounded-coordinate and zero-coordinate flags exist because those records exist, and they
will otherwise sail into your model unnoticed.

Filter on `basisOfRecord` early. Preserved specimens, human observations and machine observations
have very different error profiles and mixing them without thinking is the most common mistake we
see.

## The call

Grade A−. As infrastructure this is exemplary and the reproducibility story is genuinely
best-in-class. The mark comes off for a sample whose biases are structural rather than fixable, and
for a licence patchwork that makes downstream reuse a legal exercise as well as a technical one.
Bring your own effort correction and it is indispensable.
