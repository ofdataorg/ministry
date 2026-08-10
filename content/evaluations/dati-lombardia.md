---
title: "Open Data Regione Lombardia"
date: 2026-08-10
publishers: ["Regione Lombardia"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Governance", "Environment", "Health"]
licenses: ["CC0 1.0"]

source: "https://www.dati.lombardia.it/"
version: "Catalogue as at 10 August 2026 — 4,404 assets, 2,905 datasets; 300 sampled and downloaded"
snapshot: 2026-08-10
temporal: "Varies by dataset"
updated: "Continuously for a small live core"
cadence: "Declared on 90.3% of datasets; 27.6% of testable promises kept"
formats: ["CSV", "JSON", "GeoJSON", "RDF", "TSV"]
size: "2,905 datasets, ~54,000 columns"
access: "Open API and bulk download, no registration"

verdict: "Four hundred and forty-four datasets describe themselves as prompt. Their median age is seven years."
reviewer: "Ministry desk"

history:
  - date: 2026-08-10
    version: "Catalogue as at 10 August 2026 — 4,404 assets, 2,905 datasets"
    note: "First scoring, from catalogue metadata. Superseded the same day by [an audit of 300 randomly sampled datasets](/analyses/we-opened-six-hundred-datasets/), which found 65.4% of the catalogue shares a column schema with another dataset and 31.7% of datasets carry a wholly empty column. Completeness and interoperability revised down."
    scores: { completeness: 7, timeliness: 2, documentation: 3, accessibility: 9, licensing: 9, interoperability: 7 }

scores:
  completeness: 6
  timeliness: 2
  documentation: 3
  accessibility: 9
  licensing: 9
  interoperability: 6

strengths:
  - "**82.1% of the catalogue is CC0** — a public domain dedication as the default, which is the most permissive choice a public body can make and almost nobody makes it."
  - "Genuinely broad regional coverage: 933 transparency datasets, 544 environment, 526 statistics, 433 mobility, 251 health, across 26 categories."
  - "Same Socrata engineering as New York — no registration, a working SODA API, and CSV, JSON, GeoJSON, RDF and TSV from one endpoint."
weaknesses:
  - "**444 datasets declare their cadence as `Tempestiva` — prompt — and have a median age of 2,701 days. Four of them are actually current.**"
  - "Only 27.6% of testable cadence promises are kept overall. Weekly series sit at a median of five years, monthly at four."
  - "Half the catalogue barely describes itself: 50.1% of assets have a description under 80 characters, and only 16.0% of columns carry one."
  - "**65.4% of datasets share a column schema with another** — 2,902 datasets rest on 1,312 distinct schemas, and 884 are the same template refiled by a different comune."

bestfor:
  - "Anything where a CC0 licence removes a legal obstacle"
  - "Regional environment, health and transparency data for northern Italy"
  - "The live core — air quality and sensor feeds that are genuinely current"
avoidfor:
  - "Trusting any cadence label on this portal without checking the actual date"
  - "Analysis needing documented columns"
  - "Reading the 4,404 headline as a dataset count"
---

## What it is

Regione Lombardia's open data portal: 4,404 catalogue assets, of which 2,905 are datasets, on
Socrata. Lombardia is Italy's largest region by population and economy, and the catalogue reflects
it — 933 transparency datasets, 544 on environment, 526 statistics, 433 mobility, 370 territory,
251 health, spread across 26 categories.

Figures were measured against the Socrata Discovery API on 10 August 2026.

## How it holds up

**The licensing is genuinely excellent and deserves to lead.** 3,617 assets — 82.1% — are released
under **CC0 1.0**, a public domain dedication: no attribution required, no conditions, nothing to
comply with. A further 520 are CC BY 4.0 and 86 carry the Italian Open Data Licence 2.0. Only 173
(3.9%) state nothing.

CC0 as a default is the most permissive thing a public body can do with its data, and almost none
of them do it. Set against [New York](/evaluations/nyc-open-data/), which states no licence on 97.4%
of a comparable catalogue, Lombardia has answered the hardest question before anyone had to ask.

**And then the clock, which is the worst result we have recorded.**

90.3% of datasets declare an update frequency, which sounds like the discipline we keep asking for.
Then you test the declarations against the data:

| Declared | Datasets | Median age | Inside window |
|---|---:|---:|---:|
| Tempestiva (prompt) | 444 | **7.4 years** | **0.9%** |
| Annuale | 557 | 2.1 years | 39.1% |
| Settimanale (weekly) | 308 | 5.0 years | 36.0% |
| Mensile (monthly) | 258 | 4.3 years | 24.0% |
| Giornaliera (daily) | 134 | 13 days | 50.0% |
| Trimestrale (quarterly) | 124 | 1.6 years | 22.6% |
| Semestrale | 56 | 195 days | 51.8% |
| Mai (never) | 333 | 6.7 years | not applicable |

Of 1,881 datasets making a testable promise, **519 keep it — 27.6%.**

Look at the first row again. Four hundred and forty-four datasets are labelled *Tempestiva*, the
Italian public-sector term for data published promptly, essentially in real time. Their median age
is 2,701 days. **Four of the 444 are actually current.** The label is not merely aspirational; it is
attached to a body of data that has not moved since roughly 2019.

This is worse than saying nothing. A dataset with no stated cadence forces a reader to check the
date. A dataset labelled *Tempestiva* invites them not to. The metadata that was supposed to make
the catalogue trustworthy is actively misleading on 444 counts, and a reader who believes it will
publish a figure from 2019 thinking it describes today.

The honest part of the picture is `Mai` — never — used on 333 datasets to mark closed archives.
That is the right label, correctly applied, and it shows the vocabulary is understood. Which makes
the misuse of *Tempestiva* harder to excuse rather than easier.

Across all datasets the median was last updated 1,916 days ago — over five years — and 57.3% have
not moved in four.

**Documentation is the other weak axis.** 50.1% of assets carry a description under 80 characters,
so half the catalogue is a title and a shrug. Only 8,652 of roughly 54,000 columns have a
description — **16.0%**, the lowest column coverage we have measured.

**Two structural notes for anyone consuming the catalogue programmatically.** First, 708 of the
4,404 assets are community-contributed rather than official, and 1,248 more are filters, charts,
maps and stories — derived views, not data. The headline count is roughly half datasets. Second,
the cadence field itself is published under two different key spellings —
`Frequenza-di-aggiornamento_Frequenza` on 2,305 assets and `Frequenza_di_aggiornamento_Frequenza` on
358 — with inconsistent capitalisation in the values (`settimanale` and `Settimanale` both appear).
Any harvester that keys on one spelling silently loses a seventh of the catalogue.

## What 300 downloads showed

We drew a random sample of 300 official datasets and pulled 200 rows from each; the method and the
cross-portal comparison are in
[We Opened Six Hundred Datasets](/analyses/we-opened-six-hundred-datasets/).

Access held up: **300 of 300 downloaded**, median response 0.23 seconds — faster than New York on the
same platform. Seven returned a valid file with no rows in it, which is a catalogue entry pretending
to be a dataset, but 97.7% were usable.

The structural finding is duplication. **65.4% of Lombardia's datasets share a column signature with
another dataset**; 2,902 datasets rest on just 1,312 distinct schemas. Strip the municipality from
the titles and the templates appear: 37 *Parcheggi*, 27 *Elenco delle aree di circolazione*, 22
*Quantità rifiuti prodotta*, 20 *Aree verdi informazioni*. In total **884 datasets — 30.4% of the
catalogue — are one form refiled by a different comune.**

That is a legitimate way to publish; each comune's parking data really is its own data. But it means
breadth is far narrower than 4,404 suggests, and it explains the empty columns exactly. 31.7% of
sampled datasets carry at least one wholly empty column, and the pattern is unmistakable: `Comune di
Formigara — Parcheggi` and `Comune di Ripalta Guerina — Parcheggi` have the *same* 12 of 26 columns
blank. One template, sent to different clerks, filled in to the same depth.

Also here, as in New York: **20.6% of columns declared `Text` hold only numbers** — the identical
figure on both portals, which makes it the platform's ingest default rather than anything Lombardia
chose.

## Working with it

Ignore the cadence labels and read `data_updated_at` directly from the API. On this portal the
declared frequency has almost no predictive value, and acting on it is the single most likely way to
publish something wrong.

Filter to `provenance=official` and `type=dataset` before counting anything. Handle both spellings
of the frequency key if you harvest metadata.

The live core is real and worth using — daily-declared datasets have a median age of 13 days, and
the sensor feeds behave. It is just much smaller than the catalogue implies.

## The call

**Grade B−**, revised down within the band after the sampling. On licensing this is a model for every European regional government: CC0 by default,
applied at scale, no conditions to negotiate. The access and API engineering are as good as New
York's because they are the same platform.

It is dragged down by the gap between what the catalogue says about itself and what it is. A
27.6% compliance rate would be poor on its own; 444 datasets advertising promptness while sitting
seven years untouched is a metadata failure that misleads exactly the readers who did the right
thing and checked. Relabelling those to `Mai` would cost nothing, tell the truth, and raise this
grade immediately.
