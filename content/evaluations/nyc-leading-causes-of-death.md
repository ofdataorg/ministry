---
title: "NYC Leading Causes of Death"
date: 2026-08-10
publishers: ["NYC Department of Health and Mental Hygiene"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Health", "Population"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/jb7j-dtam"
version: "2,102 rows at snapshot; series to 2021"
snapshot: 2026-08-10
temporal: "2007 onward"
updated: "27 January 2026"
cadence: "Declares Annually, not automated"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "2,102 rows, 7 columns"
access: "Open API and bulk download, no registration"

verdict: "Age-adjusted mortality by cause, sex and ethnicity — done properly, in seven columns, with a caveat about small numbers the publisher volunteered."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 5
  documentation: 8
  accessibility: 9
  licensing: 3
  interoperability: 8

strengths:
  - "**Age-adjusted rates are published alongside crude rates and raw counts.** For mortality compared across ethnic groups with different age structures, that is the difference between an analysis and a mistake."
  - "All 7 columns documented, and the description warns that rates based on small numbers are unstable — a limitation volunteered rather than discovered."
  - "Tidy long format: year, cause, sex, ethnicity, deaths, rate, adjusted rate. Nothing to reshape."
weaknesses:
  - "The file carries `Report last ran: 09/24/2019` in its description while the portal shows it modified in January 2026, so it is unclear which date describes the data."
  - "Data reaches 2021 on a dataset declaring an annual cadence, leaving several years unaccounted for."
  - "Cause labels carry trailing whitespace — `Intentional Self-Harm ` — which will silently split groups in a naive `GROUP BY`."

bestfor:
  - "Mortality disparities by ethnicity and sex, correctly age-adjusted"
  - "Long-run cause-of-death trends for a large US city"
avoidfor:
  - "Current-year mortality"
  - "Grouping on the cause label without trimming it first"
---

## What it is

The leading causes of death in New York City since 2007, broken down by sex and race/ethnicity, with
counts, crude death rates and age-adjusted death rates. 2,102 rows and 7 columns, derived from the
death certificate issued for every death occurring in the city.

Small, tidy, and doing the thing that mortality statistics most often get wrong.

## How it holds up

**Publishing the age-adjusted rate is the single most important decision here and they made it.**
Mortality compared across ethnic groups is dominated by age structure — a younger population will
show fewer deaths per capita from almost everything, regardless of health. Comparing crude rates
across groups produces confident, published, wrong conclusions. This dataset ships
`age_adjusted_death_rate` next to `death_rate` and `deaths`, so a reader who does the obvious thing
does the right thing.

All seven columns are documented, and the description goes further, warning that rates based on
small numbers are unstable and should be interpreted with caution. That is a limitation the
publisher volunteered about their own data. Our documentation axis exists to reward exactly this.

The shape is properly long — one row per year, cause, sex and ethnicity — so it loads and groups
without reshaping.

**The dating is confusing.** The description states `Report last ran: 09/24/2019`. The portal's own
`data_updated_at` says January 2026. The most recent year in the data is 2021. Three different dates
tell three different stories, and a reader cannot easily determine which describes the figures they
are holding. Declaring an annual cadence while the series stops at 2021 leaves several years
unexplained.

**One small trap that will bite.** Cause labels carry trailing spaces — we found
`Intentional Self-Harm ` with a trailing blank. A `GROUP BY leading_cause` will split that from any
correctly-trimmed variant elsewhere in the file, quietly halving a count. Trim before grouping.

## Working with it

Use `age_adjusted_death_rate` for any comparison between groups, and `deaths` for anything you need
to sum. Do not mix them.

Trim whitespace on `leading_cause`, `sex` and `race_ethnicity` on load.

Treat suppressed or tiny cells with the caution the publisher asks for; the warning is there because
the file contains cells in single digits.

## The call

**Grade B.** Methodologically this is a small dataset doing the hard thing right — age adjustment
published, limitations stated, structure tidy. It loses ground on a series that stops several years
short of its declared annual cadence and on three conflicting dates that leave a reader unsure what
period they are looking at.
