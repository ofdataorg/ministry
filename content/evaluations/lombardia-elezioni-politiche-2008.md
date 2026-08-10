---
title: "Lombardia — 2008 General Election Results by Municipality"
date: 2026-08-10
publishers: ["Regione Lombardia"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Governance", "Society"]
licenses: ["CC0 1.0"]

source: "https://www.dati.lombardia.it/d/w32m-yybv"
version: "2008 Camera dei Deputati result — 1,546 municipalities"
snapshot: 2026-08-10
temporal: "13–14 April 2008"
updated: "5 July 2012"
cadence: "Declares Mai (never) — correct; an election result is fixed"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "1,546 municipalities, 28 columns"
access: "Open API and bulk download, no registration"

verdict: "A complete, permanent, CC0 election result — with the parties as column headings, so it will never stack with another year."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 7
  documentation: 2
  accessibility: 9
  licensing: 9
  interoperability: 6

strengths:
  - "Complete for its scope: all 1,546 Lombard municipalities for the 2008 Chamber of Deputies election, with electorate, turnout, valid papers and blanks alongside the party votes."
  - "`Mai` is exactly the right cadence label and this is what correct use of it looks like — a 2008 result is finished, and saying so is more useful than implying maintenance."
  - "CC0, ungated, and joinable through `codice_comune` and `codice_provincia`."
weaknesses:
  - "**Each party is its own column** — `lega_nord`, `p_democratico`, `sinistra_arcobaleno`, `forza_nuova`, `fiamma_tricolore` — so the schema is election-specific and cannot be stacked with any other year."
  - "Zero of 28 columns documented, which leaves the distinction between `numero_votanti`, `schede_valide` and `schede_bianche` to be inferred."
  - "Published in 2012 for a 2008 election and never revisited, with no link to sibling datasets for other elections."

bestfor:
  - "Historical Italian electoral geography at municipal level"
  - "Joining 2008 vote shares to census or economic data by comune"
avoidfor:
  - "Multi-election time series, without transposing the party columns first"
  - "Assuming column presence implies a party stood everywhere"
---

## What it is

The 2008 Italian general election result for the Chamber of Deputies, broken down by every
municipality in Lombardia: 1,546 rows, 28 columns. Electorate, voters, valid papers, blank papers,
and then one column per party — Lega Nord, Partito Democratico, Sinistra Arcobaleno, Italia dei
Valori, Fiamma Tricolore, Forza Nuova, Partito Liberale, and a scattering of minor lists down to
Unione Consumatori.

## How it holds up

**On completeness and honesty it does well.** Every Lombard comune is present, the turnout
denominators are there alongside the party votes, and the cadence declaration is `Mai` — never
updated.

That label is correct and worth pausing on. The 2008 result is a fact that will not change. A
publisher who marks it `Mai` is telling the reader something true and useful, and a reader who sees
a fourteen-year-old file with an honest "this is final" label knows exactly where they stand. It is
the same vocabulary that 444 datasets on this portal
[misuse](/evaluations/dati-lombardia/), used properly.

**The shape is the problem, and it is a structural one.** Parties are columns. `lega_nord` is a
field name. `p_democratico` is a field name.

This works perfectly for one election and fails completely across several. The 2013 result has
different parties; so does 2018; so does 2022. Each election therefore needs its own schema, and no
two can be concatenated without first transposing every party column into rows of `partito` and
`voti`. Anyone studying electoral change over time — which is most of what municipal election data
is *for* — has to do that transposition for every year before they can begin.

The long form would have been three columns wide, stacked across every election Italy has held, and
would still be growing. The wide form is a spreadsheet frozen at the moment it was made.

It also hides absence. A party that did not stand in a municipality and a party that stood and
polled zero are both a `0` in this layout, and nothing distinguishes them.

**Documentation is zero of 28 columns.** For party columns the names carry the meaning. For the
administrative ones they do not: `numero_elettori`, `numero_votanti`, `schede_valide` and
`schede_bianche` stand in a specific arithmetic relationship that determines whether turnout is
computed correctly, and none of it is written down.

## Working with it

Melt the party columns immediately into `partito` / `voti`, and keep the administrative columns as
identifiers. That done, it stacks with any other election you have similarly reshaped.

Verify the turnout arithmetic on a few rows before trusting it — check whether valid plus blank plus
spoilt reconciles to voters — and record what you find, since the file will not tell you.

## The call

**Grade B.** A complete, permanent, openly licensed municipal election result, correctly labelled as
final. The substance is sound and the licence is the best available.

It loses ground for a layout that guarantees every future user must reshape it before it can be
compared with any other election, and for leaving the relationship between its four turnout columns
entirely to inference.
