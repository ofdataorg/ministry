---
title: "DATASUS SIM — Brazilian Mortality Information System"
date: 2026-05-28
publishers: ["Ministério da Saúde (DATASUS)"]
regions: ["South America"]
domains: ["Health", "Population"]
licenses: ["Open, terms not clearly stated"]

source: "https://datasus.saude.gov.br/"
temporal: "1979 to present"
updated: "Annual consolidation, preliminary files earlier"
cadence: "Annual, with multi-year revision of provisional records"
formats: ["DBC (compressed DBF)", "CSV via third-party tooling"]
size: "Tens of millions of individual death records"
access: "Public FTP and web tabulators, no registration"
verdict: "Four decades of individual-level mortality for a continent-sized country, locked inside a file format almost nobody else uses."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 5
  documentation: 4
  accessibility: 4
  licensing: 6
  interoperability: 3

strengths:
  - "Record-level, not aggregated: age, sex, municipality, cause of death coded to ICD-10, from 1979."
  - "Municipality-level geography across the whole country makes fine-grained spatial epidemiology genuinely possible."
  - "Coverage has improved dramatically over the series and is now high in most states."
weaknesses:
  - "DBC is a Brazil-specific compressed DBF variant. No mainstream tool reads it without a community package."
  - "Documentation is fragmented across PDFs, ministry notes and academic papers, largely in Portuguese, and describes the codebook rather than the caveats."
  - "Coverage and cause-of-death quality vary substantially by state and by decade — ill-defined causes remain non-trivial in parts of the North and Northeast."

bestfor:
  - "Municipality-level mortality and cause-of-death epidemiology"
  - "Long-run Brazilian health trends"
  - "Excess mortality work with a genuine baseline"
avoidfor:
  - "Naive interstate comparisons that ignore coverage differences"
  - "Recent-year analysis before the file is consolidated"
  - "Any pipeline that cannot tolerate a bespoke binary format"
---

## What it is

SIM — the Sistema de Informações sobre Mortalidade — is Brazil's national death registration
database, published at the level of the individual record since 1979. Each row is one death: age,
sex, race/colour, municipality of residence and occurrence, underlying cause coded to ICD-10, plus
a long tail of certificate fields.

For a country of over 200 million people this is an extraordinary public asset. Very few
middle-income countries publish individual-level mortality microdata at all, let alone a series four
decades deep with municipality geography.

## How it holds up

The substance scores well. The value of record-level data with fine spatial resolution is enormous,
and the series is long enough to support real historical work. Coverage has improved markedly since
the 1990s and is now high across most of the country.

Everything about *getting to it* scores badly, and the gap between those two facts is the story of
this evaluation.

The files ship as DBC — a compressed variant of DBF specific to the Brazilian health ministry. It is
not a format any standard tool reads. Working with SIM means first installing a community package
(the R `read.dbc` lineage, or the Python ports) whose maintenance depends on a small number of
volunteers. A national statistical asset should not have a bus factor.

Documentation is a codebook problem and a caveat problem. The codebook exists, mostly in Portuguese,
scattered across PDFs and ministry notes. What is much harder to find is the guidance a careful
analyst needs: which states under-registered in which decade, how the ill-defined-cause share moved,
what the redistribution conventions are, when a variable's coding changed. That knowledge lives in
the Brazilian epidemiology literature rather than with the data, which means every new user either
already has a supervisor who knows or is about to publish something wrong.

Licensing is the quiet weakness. The data is public and freely downloadable and everyone treats it
as open — but the terms are not clearly stated in a way an institution's lawyer would accept. It is
open in practice and ambiguous on paper.

## Working with it

Pull from the FTP rather than the web tabulator; the tabulator is fine for a single figure and
useless for analysis. Convert DBC to something durable — Parquet — as your first pipeline step, and
keep the raw files. Expect to spend real time on the municipality code changes across the series, and
do not compare states on crude coverage without adjusting.

Wait for the consolidated annual file before publishing anything on a recent year. Preliminary data
moves, sometimes materially.

## The call

Grade C+. The underlying asset would score highly on substance alone — this is data most countries
do not publish. What drags it down is everything wrapped around it: a bespoke binary format, caveats
that live in journals instead of the documentation, and licence terms nobody has bothered to state.
None of that is hard to fix, which is what makes it frustrating rather than forgivable.
