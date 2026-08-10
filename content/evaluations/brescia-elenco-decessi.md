---
title: "Comune di Brescia — Elenco Decessi"
date: 2026-08-10
publishers: ["Comune di Brescia"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Population", "Health"]
licenses: ["CC0 1.0"]

source: "https://www.dati.lombardia.it/d/avft-pty4"
version: "833 aggregate rows at snapshot; last refreshed April 2024"
snapshot: 2026-08-10
temporal: "Deaths recorded from 1800 onward"
updated: "10 April 2024"
cadence: "Declares Giornaliera (daily); 852 days since it last moved"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "833 rows, 4 columns"
access: "Open API and bulk download, no registration"

verdict: "The most-viewed dataset on the Lombardia portal declares itself daily, has not moved in two years, and explains none of its four columns."
reviewer: "Ministry desk"

scores:
  completeness: 5
  timeliness: 2
  documentation: 1
  accessibility: 9
  licensing: 9
  interoperability: 5

strengths:
  - "CC0 — a public domain dedication on civil registry statistics, with nothing to comply with."
  - "Tiny and fast: 833 rows over the API instantly, in a tidy long shape."
  - "The counts reach back to 1800, so the underlying registry work behind it is substantial."
weaknesses:
  - "**It declares `Giornaliera` — daily — and has not been touched for 852 days.** It is also the single most-viewed dataset on the portal, at 177,793 page views."
  - "**Zero of four columns documented**, on a file where `occorrenze` is doing all the analytical work."
  - "The title, *Elenco Decessi* — list of deaths — describes a register. What is published is a frequency table of counts by year, citizenship and sex."

bestfor:
  - "Aggregate death counts for Brescia by year, sex and citizenship"
  - "A cautionary example of what a cadence label is worth unchecked"
avoidfor:
  - "Anything expecting individual death records, whatever the title suggests"
  - "Recent mortality — the file stops in 2024 and was never daily"
---

## What it is

Four columns — `anno_di_morte`, `cittadinanza`, `sesso`, `occorrenze` — and 833 rows. Year of death,
citizenship, sex, and a count. The earliest row we found records a single death in the year 1800.

It is the most-viewed dataset on the entire Regione Lombardia portal: 177,793 page views, ahead of
anything the region itself publishes. That is what makes its condition worth writing about.

## How it holds up

**Start with the title, because it sets a false expectation.** *Elenco Decessi* means "list of
deaths". A list implies a register — one row per death, as
[DATASUS](/evaluations/datasus-sim-mortality/) publishes for Brazil. This is not that. It is an
aggregate frequency table: for each combination of year, citizenship and sex, how many deaths were
recorded. 833 rows cannot be a list of deaths in a city of 200,000 spanning two centuries, and a
user who downloads it expecting microdata has to work that out for themselves.

**The cadence declaration is simply false.** The metadata says `Giornaliera` — daily. The data was
last processed on 10 April 2024, **852 days** before we looked. This is the failure we documented
across the portal in the [Lombardia evaluation](/evaluations/dati-lombardia/), where 444 datasets
declare themselves prompt at a median age of seven years. Here it lands on the portal's single most
consulted file.

The combination is what makes it serious. A daily label on an obscure dataset misleads few people. A
daily label on the most-viewed dataset on the portal misleads everyone who arrives, and 177,793
page views is a lot of arrivals.

**Zero of four columns are documented**, which on a four-column file sounds survivable and is not.
`occorrenze` — occurrences — is the count, and nothing states what it counts: deaths registered in
Brescia, deaths of Brescia residents wherever they occurred, or deaths recorded in the comune's
archive. Those are three different denominators and the distinction decides whether any rate
computed from this is meaningful. `cittadinanza` is a nationality string with no stated vocabulary.

**The licence, by contrast, is exemplary.** CC0, no conditions — the correct choice for civil
registry aggregates, and better than most of Europe manages.

## Working with it

Treat it as what it is: an aggregate table, not a register. Before computing any rate, establish
what `occorrenze` counts by asking the comune, because the file will not tell you and the answer
changes the result.

Ignore the cadence field entirely and read `data_updated_at`.

Historical rows — the eighteenth and nineteenth century counts — are almost certainly a digitised
archive with different completeness from modern registration. Do not plot them on one axis with
recent years without saying so.

## The call

**Grade C+.** The licence is the best available and the underlying archival work reaching back to
1800 is real. Everything about the publication works against the reader: a title that describes a
different kind of file, a daily label on a dataset frozen for over two years, and no explanation of
the one column that carries the meaning.

It is the most-viewed dataset on its portal. Four sentences of documentation and an honest cadence
label would fix nearly all of it, and would be repaid more here than anywhere else on the site.
