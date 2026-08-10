---
title: "We Opened Six Hundred Datasets"
date: 2026-08-10
author: "Ministry desk"
description: "A random sample of 300 datasets from New York and 300 from Lombardia, downloaded and profiled. The catalogue and the contents are not the same thing."
domains: ["Governance"]
regions: ["North America", "Europe"]
places: ["Global"]
toc: true
---

Catalogue metadata tells you what a portal claims. It does not tell you what happens when you press
download. So we drew a random sample of 300 official datasets from
[NYC Open Data](/evaluations/nyc-open-data/) and 300 from
[Regione Lombardia](/evaluations/dati-lombardia/), pulled 200 rows from each through the SODA API,
and profiled the results. Six hundred downloads, one seeded random sample per portal, on 10 August
2026.

Both portals run the same software. That turned out to be the most useful thing about the exercise:
where the two agree, you are looking at the platform; where they diverge, you are looking at the
institution.

## The data is actually there

Start with the good news, because it is not guaranteed and it is not trivial.

| | New York | Lombardia |
|---|---:|---:|
| Downloaded successfully | 299 / 300 | 300 / 300 |
| Returned zero rows | 0 | 7 |
| **Usable** | **99.7%** | **97.7%** |
| Median response | 0.66 s | 0.23 s |

One NYC dataset returned a server error. Seven Lombardia datasets returned a valid, empty file — a
catalogue entry, a schema, and no rows. Everything else opened, parsed, and contained data, in well
under a second.

That sounds like a low bar. It is not. Both portals are serving thousands of datasets over an API
with no key, no gate and no rate-limit theatre, and getting it right 98% of the time. Whatever else
follows, the plumbing works.

## One column in five is mistyped, on both portals

Socrata records a declared type for every column. We took 120 datasets from each portal, found every
column declared as `Text`, and checked what was actually in it.

| | New York | Lombardia |
|---|---:|---:|
| Columns declared `Text` | 1,350 | 757 |
| Holding only numbers | 278 | 156 |
| **Share mistyped** | **20.6%** | **20.6%** |

Identical to the decimal. Two governments, two continents, two languages, two entirely separate
publishing cultures — and exactly the same proportion of numeric columns declared as text.

That is not a coincidence and it is not an indictment of either city. It is the ingest default. When
a spreadsheet arrives and nobody explicitly assigns types, the safe machine choice is `Text`, and
the safe machine choice is what everyone gets. The consequence lands on every consumer: a fifth of
the numeric columns on both portals will sort `"10"` before `"9"` and refuse to sum until cast.

Where the platform decides, the platform's default becomes the standard — and nobody chose it.

## Published columns that contain nothing

Across the sample we counted columns that were entirely empty in every row returned.

| | New York | Lombardia |
|---|---:|---:|
| Wholly empty columns | 996 of 8,067 | 392 of 4,227 |
| Share of all columns | 12.3% | 9.3% |
| Datasets with at least one | 18.1% | **31.7%** |
| Datasets over half empty | 4.3% | 2.7% |

New York has more empty columns; Lombardia spreads them across more datasets. Both matter, and they
have different causes.

New York's are concentrated in a handful of enormous survey exports. The worst is the **2020 DOE
Middle School Directory: 333 of its 464 columns are entirely empty**, and 88% of all its cells are
blank. The 2017 High School Directory manages 191 of 462. These are wide school-survey instruments
dumped whole, with every question that was not asked of every school left in place as a column.
Nothing is wrong with the rows that exist; the schema is simply four times larger than the data.

Lombardia's empty columns come from somewhere else entirely, and finding out where was the most
interesting result of the exercise.

## Two thirds of Lombardia is the same handful of forms

We hashed the column signature of every dataset on both portals and counted how many share one.

| | New York | Lombardia |
|---|---:|---:|
| Datasets | 2,396 | 2,902 |
| Distinct schemas | 2,052 | **1,312** |
| Sharing a schema with another dataset | 22.2% | **65.4%** |

Two thirds of Lombardia's catalogue is schema-duplicated. Strip the municipality prefix from the
titles and the pattern is obvious: 37 datasets called *Parcheggi*, 27 *Elenco delle aree di
circolazione*, 22 *Quantità rifiuti prodotta*, 20 *Aree verdi informazioni*, 20 *Autoscuole*. In
total **884 datasets — 30.4% of the catalogue — are the same template refiled by a different
comune.**

This is not fraud and it is not padding in any deliberate sense. Italian transparency obligations
push a standard schema down to every municipality, each publishes its own instance, and the regional
portal aggregates them. A parking dataset for Formigara genuinely is different data from a parking
dataset for Ripalta Guerina.

But it explains the empty columns exactly. The template has 26 fields; a village of two thousand
people fills in eleven. We found `Comune di Formigara — Parcheggi` and `Comune di Ripalta Guerina —
Parcheggi` with an identical 12 of 26 columns blank, because they are the same form, sent to
different clerks, filled in to the same depth.

It also means the headline number is a poor guide to breadth. Lombardia advertises 4,404 assets.
Under 3,000 are datasets, and those rest on 1,312 distinct schemas. That is still a substantial
catalogue. It is not the one the number implies.

## Fresh data is emptier than stale data

The result we did not expect. We split each sample by whether the dataset had been updated in the
last four years and compared how empty the cells were.

| Mean cell emptiness | New York | Lombardia |
|---|---:|---:|
| Updated within 4 years | 11.1% | 14.7% |
| Not updated in 4+ years | 7.7% | 11.6% |

On both portals, the *maintained* datasets are emptier than the abandoned ones. Consistently, and in
the same direction.

The explanation is not that fresh data is worse. It is that the two populations are different kinds
of object. A live operational feed — service requests, permits, inspections — carries fields that
only apply to some records: a closing date that is null until the case closes, a resolution code
that is null until someone resolves it. Emptiness there is the data behaving correctly.

A stale dataset is usually a finished extract: someone ran a query once, exported the result, and
walked away. Extracts are dense because the query already dropped what was missing.

So cell emptiness measures *what kind of thing you are holding* far more reliably than it measures
quality. Which is worth saying plainly, because emptiness is exactly the metric an automated quality
score would reach for first, and it would rank a dead spreadsheet above a working system.

## What we took from it

**Sampling beats browsing.** Every finding here required opening files. None of it is visible from
the catalogue, and some of it directly contradicts what the catalogue implies.

**Where a platform decides, the platform's default becomes policy.** The identical 20.6% mistyping
rate in New York and Lombardia was not decided by anyone in either government.

**Count schemas, not datasets.** A dataset count measures publishing activity. A schema count is
closer to measuring how much distinct information is on offer, and for Lombardia the two differ by
more than a factor of two.

**Simple quality metrics point the wrong way.** Null density, the most obvious automated measure,
would systematically rank abandoned extracts above maintained services on both portals.

Both evaluations have been re-scored on this evidence, with the previous grades left visible on the
page so the movement can be seen. Neither moved much, and both moved down: opening the files
generally tells you less good news than reading about them.
