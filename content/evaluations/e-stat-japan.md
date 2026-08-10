---
title: "e-Stat — Portal Site of Official Statistics of Japan"
date: 2026-05-19
publishers: ["Statistics Bureau of Japan"]
regions: ["Asia"]
place: "Japan"
places: ["Japan"]
domains: ["Economy", "Population"]
licenses: ["Japan Government Standard Terms (CC BY 4.0 compatible)"]

source: "https://www.e-stat.go.jp/en"
temporal: "Varies; census series back to 1920"
updated: "Continuously, per agency"
cadence: "Per-survey release schedules"
formats: ["CSV", "Excel", "API (JSON/XML)"]
size: "Tens of thousands of statistical tables from all central government agencies"
access: "Open; free API key required for programmatic access"
verdict: "One of the most complete official statistical systems in the world, published as spreadsheets designed to be looked at rather than read."
reviewer: "Ministry desk"

scores:
  completeness: 9
  timeliness: 7
  documentation: 6
  accessibility: 6
  licensing: 8
  interoperability: 4

strengths:
  - "Genuinely comprehensive: every central agency publishes through one portal, with a century-deep census series behind it."
  - "A documented API with stable statistical table identifiers, which is more than many peers offer."
  - "Standard government terms of use are permissive and CC BY 4.0 compatible."
weaknesses:
  - "Tables are laid out for human reading — merged cells, multi-row headers, notes inside data cells, totals interleaved with detail."
  - "English coverage is partial and inconsistent; the deeper you go, the more Japanese-only it becomes."
  - "Municipal codes change with every merger and the historical crosswalks are not shipped with the data."

bestfor:
  - "Authoritative Japanese demographic and economic series"
  - "Long-run census work, given patience with historical geography"
  - "Cross-agency questions that would otherwise mean chasing ten websites"
avoidfor:
  - "Automated ingestion without a hand-written parser per table family"
  - "English-only workflows below the headline indicators"
  - "Municipal time series across merger waves without a crosswalk"
---

## What it is

e-Stat is the single portal for Japanese official statistics: the census, labour force survey,
economic census, vital statistics, agriculture, trade — output from every central agency, in one
place, with an API in front of it. On coverage it is close to best in class. Japan's statistical
system is thorough, long-running and well funded, and e-Stat exposes essentially all of it.

## How it holds up

Completeness scores a nine and earns it. If a Japanese government body collected it, it is here.
The census series reaches back to 1920, survey documentation exists, and the release cadence is
predictable.

Interoperability scores a four, and that is the axis that will decide your week.

The problem is a philosophy of publication. Tables are built as *documents* — designed to be
printed or read on screen — rather than as data. That means merged header cells, two or three rows
of stacked column labels, category totals interleaved with their own components, footnote markers
sitting inside numeric cells, and blank spacer columns for visual rhythm. Every one of those is fine
for a human reader and fatal to `read_csv`. Getting a tidy frame out of a typical e-Stat table means
writing a bespoke parser, and the next table family will need a different one.

The API helps but does not solve it. It gives you reliable access to the same document-shaped
tables. Retrieval is automated; reshaping is not.

Language is the second friction. The English interface covers the portal and the major indicators
well. Below that, table titles, category labels and notes are Japanese-only, and machine-translated
category labels are exactly where silent misclassification happens. This is a legitimate choice by a
national statistics office serving its own public first — but it is a real constraint on
international reuse and we score what users encounter.

Municipal geography is the third. Japan's Heisei-era municipal mergers reshaped local government
extensively, codes changed accordingly, and the crosswalks needed to build a consistent municipal
time series are not distributed alongside the statistics.

## Working with it

Get an API key, work from stable table IDs, and write one parser per table family rather than hoping
for a general solution. Cache aggressively; you will be re-running the reshape more often than the
fetch. Keep a municipality crosswalk beside you at all times and treat any municipal series that
crosses a merger year as suspect until proven otherwise.

## The call

Grade B−. The statistical substance deserves considerably better and the coverage is genuinely
excellent. The score reflects the cost of extraction: spreadsheets built for eyes, partial English
below the surface, and historical geography left as an exercise for the reader. Publish the same
content as tidy tables and this jumps a full grade overnight.
