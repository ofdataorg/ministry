---
title: "Eurostat Database"
date: 2026-06-05
publishers: ["Eurostat"]
regions: ["Europe"]
domains: ["Economy", "Population", "Environment"]
licenses: ["CC BY 4.0"]

source: "https://ec.europa.eu/eurostat/data/database"
temporal: "Varies by table; many series from the 1960s"
updated: "Continuously, per table"
cadence: "Per-indicator release calendar, published in advance"
formats: ["TSV", "SDMX", "JSON API"]
size: "Thousands of multidimensional tables"
access: "Open API and bulk download, no registration"
verdict: "Harmonised statistics for a continent, wrapped in a navigation experience that punishes the curious."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 7
  documentation: 8
  accessibility: 6
  licensing: 9
  interoperability: 7

strengths:
  - "Genuine cross-country harmonisation with documented methodology — comparability is engineered, not assumed."
  - "NUTS regional geography is stable, versioned and joinable to official boundary files."
  - "Release calendars are published ahead of time, so pipelines can be scheduled rather than polled."
weaknesses:
  - "Finding the right table code is an expedition. The browser is a tree of thousands of nodes and search rarely lands where you want."
  - "Flag characters (`p` provisional, `e` estimated, `b` break in series, `:` not available) are embedded in value fields and break naive parsers."
  - "NUTS boundaries are revised every few years and series are not always back-cast, silently fracturing regional time series."

bestfor:
  - "Comparable indicators across EU and EFTA members"
  - "Regional analysis at NUTS 2 and NUTS 3"
  - "Official denominators for anything European"
avoidfor:
  - "Long regional time series across a NUTS revision without checking for breaks"
  - "Quick answers if you do not already know the table code"
  - "Sub-national coverage outside the harmonised NUTS framework"
---

## What it is

The statistical office of the European Union publishing thousands of harmonised tables: national
accounts, labour force, migration, energy, waste, agriculture, health. The harmonisation is the
product. Member states collect according to agreed definitions and Eurostat enforces them, which is
why an unemployment rate from Portugal and one from Estonia can sit in the same chart without an
asterisk.

## How it holds up

On substance, very well. Methodology is documented per domain, revisions are flagged, and the
advance release calendar means an automated pipeline can be scheduled against known dates instead of
polling hopefully. The SDMX and JSON APIs are serviceable and the bulk download facility works.

Accessibility is where it loses real ground, and the problem is navigation rather than availability.
Everything is open; almost nothing is findable. Table codes like `nama_10_gdp` and `demo_r_pjangrp3`
are the true primary keys of the system, and the path to discovering the one you need runs through a
tree browser with thousands of nodes and a search that reliably returns the wrong branch. Practical
users end up keeping a private list of codes, which is a strong signal that discovery has failed.

Two data-shape traps catch everyone once. Values arrive with observation flags attached in the same
field — `1234 p`, `: ` for missing — so a column read as numeric will either error or coerce to
nulls depending on how forgiving your parser is. And NUTS regional geography is revised on a cycle;
a region's code and its territory can both change between vintages. Series are not consistently
back-cast, so an innocent regional time series can contain a discontinuity that has nothing to do
with the phenomenon being measured.

## Working with it

Get the table code first, from a colleague, a paper or the bulk facility's index, and go straight to
the API. Parse flags into their own column before casting values. Pin the NUTS vintage explicitly and
check `nuts_version` against every boundary file you join to. If a regional series jumps at 2016 or
2021, suspect the geography before you suspect the economy.

## The call

Grade B+. The statistical work underneath is strong, harmonisation is real and hard-won, and the
licensing is clean. The score is held back by a discovery experience that turns a five-minute task
into an afternoon, and by encoding conventions that were designed for a spreadsheet era and still
trip every new user exactly once.
