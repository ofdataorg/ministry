---
title: "American Community Survey"
date: 2026-06-14
publishers: ["United States Census Bureau"]
regions: ["North America"]
places: ["United States"]
domains: ["Population", "Economy", "Housing"]
licenses: ["US Public Domain"]

source: "https://www.census.gov/programs-surveys/acs"
temporal: "2005 to present (5-year estimates from 2009)"
updated: "Annually"
cadence: "1-year and 5-year estimates released each autumn"
formats: ["CSV", "API (JSON)", "Summary files", "PUMS microdata"]
size: "Thousands of tables down to block-group geography"
access: "Open API and bulk download, no registration"
verdict: "The reference implementation of a public statistical product: every estimate ships with the uncertainty attached."
reviewer: "Ministry desk"

scores:
  completeness: 9
  timeliness: 7
  documentation: 10
  accessibility: 9
  licensing: 10
  interoperability: 9

strengths:
  - "Margins of error published for every single estimate. Not an appendix — a column."
  - "Documentation is exhaustive and honest, including about its own limitations and disclosure controls."
  - "A stable, free, well-designed API plus PUMS microdata for anyone who needs to build their own tabulations."
weaknesses:
  - "5-year estimates are a five-year average, and readers treat them as a point-in-time measurement constantly."
  - "Small-area estimates carry margins of error that can exceed the estimate itself — statistically honest, practically unusable."
  - "Disclosure avoidance introduces controlled noise at fine geographies, and its interaction with small-area analysis is still contested."

bestfor:
  - "Small-area demography with quantified uncertainty"
  - "Longitudinal comparison of US social and economic conditions"
  - "Building custom tabulations from microdata"
avoidfor:
  - "Year-on-year change at block-group level"
  - "Treating 5-year estimates as current-year figures"
  - "Anything outside the United States, obviously"
---

## What it is

A continuous household survey covering roughly 3.5 million addresses a year, published as 1-year
estimates for larger geographies and 5-year pooled estimates all the way down to block groups. It
is the backbone of American demographic, housing and economic analysis, and the input to formulas
that distribute enormous sums of public money.

## How it holds up

This is the highest documentation score we have awarded, and it is not close. Every table has a
technical definition, every estimate has a margin of error published alongside it, sampling and
weighting methodology is public, and the Bureau publishes clear guidance on the mistakes users
actually make. When a product changes — as the 2020 experimental 1-year estimates did — the caveats
arrive loudly and in advance rather than in a footnote afterwards.

The reason it is not a straight A+ has almost nothing to do with the Bureau's craft and almost
everything to do with what happens downstream. Two problems recur.

First, the 5-year estimate is an average over sixty months. It is not "2024 data". A neighbourhood
that gentrified in 2023 appears half-gentrified for years afterwards. Journalists, consultants and
dashboards misread this weekly.

Second, at fine geography the margins of error are frequently larger than the differences people
want to report. The Bureau tells you this clearly, in the data, in a column. It is then ignored,
and rankings of census tracts get published on differences that are pure noise. The dataset behaves
correctly; the ecosystem around it often does not.

Disclosure avoidance is the live methodological argument. Protecting respondent confidentiality at
block-group resolution requires injecting controlled error, and the research community continues to
debate what that does to small-area inference. It is a genuine trade-off honestly made, but it is a
trade-off, and analysts working at fine geography should know it is there.

## Working with it

Use the API rather than downloading summary files; it is fast, stable and well documented. Always
pull the margin-of-error variable alongside the estimate and propagate it — the Bureau publishes
the formulas for aggregating MOEs and there is no excuse for dropping them. If your question needs
a cross-tabulation the published tables do not offer, go to PUMS rather than deriving something
unsound from the summary tables.

Never compare overlapping 5-year periods as if they were independent observations. They share up to
four years of sample.

## The call

Grade A. As a piece of statistical publishing this is close to the state of the art, and the
uncertainty discipline should be the standard every national statistics office is held to. The lost
marks are for a release lag that is inherent to the design and for a 5-year product whose meaning
the world persistently misunderstands.
