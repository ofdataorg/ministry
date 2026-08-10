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
version: "833 aggregate rows at snapshot; series 1979–2024, last refreshed April 2024"
snapshot: 2026-08-10
temporal: "Substantive series from 1979; stray records back to 1800"
updated: "10 April 2024"
cadence: "Declares Giornaliera (daily); 852 days since it last moved"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "833 rows, 4 columns"
access: "Open API and bulk download, no registration"

verdict: "Built so a city could count its own pandemic dead, and abandoned two years later while smaller comuni keep the identical file current to this week."
reviewer: "Ministry desk"

corrections:
  - date: 2026-08-10
    text: "The first version of this evaluation said the counts *reach back to 1800, so the underlying registry work behind it is substantial*. That was wrong and we had not checked it. There is exactly **one** death recorded before 1950 and eleven before 1979; the substantive series runs 1979–2023. It also treated the dataset's 177,793 page views as merely ironic, having missed why they are there — Brescia was among the worst-hit places in Europe in the first COVID wave, and this is the file people used to measure it. Completeness and interoperability re-scored upward; the section on the pandemic is new."

history:
  - date: 2026-08-10
    version: "833 aggregate rows; last refreshed April 2024"
    note: "First scoring, before we tested the series or understood its pandemic role. Completeness was marked down on a mistaken reading of its historical depth, and interoperability undervalued for what is in fact a clean, tidy, immediately usable table."
    scores: { completeness: 5, timeliness: 2, documentation: 1, accessibility: 9, licensing: 9, interoperability: 5 }

scores:
  completeness: 7
  timeliness: 2
  documentation: 1
  accessibility: 9
  licensing: 9
  interoperability: 6

strengths:
  - "**A usable 45-year excess-mortality series.** We measured 2,968 deaths in 2020 against a 2015–19 mean of 2,165 — **+37.1%** — with 2021 at +17.9% and 2022 at +15.3%. The pandemic is legible in four columns."
  - "Broken down by sex and by citizenship, with 27 nationalities present in 2020, so differential mortality is at least approachable."
  - "CC0, instant over the API, tidy long format — nothing between a reader and the number."
weaknesses:
  - "**It stopped on 10 April 2024 and still declares itself `Giornaliera` — daily.** 852 days, on the most-viewed dataset on the entire Lombardia portal."
  - "**Zero of four columns documented**, on a file whose entire analytical weight sits in `occorrenze` — and nothing states whether it counts deaths *in* Brescia or deaths *of* residents."
  - "Annual granularity only. The first wave killed within weeks, and a yearly total cannot show a March."

bestfor:
  - "Excess mortality for Brescia, 1979 onward, at annual resolution"
  - "A worked example of open data mattering, and of the process not outlasting the emergency"
avoidfor:
  - "Anything after 2023 — the 2024 figure is a partial year"
  - "Within-year pandemic analysis; the resolution cannot support it"
  - "Rates, until you establish what `occorrenze` counts"
---

## What it is

Four columns — year of death, citizenship, sex, and a count — and 833 rows covering Brescia from
1979 to a partial 2024. It is the most-viewed dataset on the Regione Lombardia portal, at 177,793
page views, ahead of anything the region publishes about itself.

That number is not an accident, and our first pass at this evaluation failed to explain it.

## Why anyone was looking

Brescia was among the worst-hit places in Europe in the first wave of COVID-19. In March and April
2020 the province's hospitals and its civil registry were overwhelmed, and the question everybody
wanted answered — how many more people are dying than normally would — could not be answered from
cause-of-death reporting, which was slow, contested and incomplete.

Excess mortality answered it instead. You do not need to know what killed someone to count that they
died, and you do not need to trust anyone's case definition. All you need is a long, consistent
series of total deaths. This file is that series.

It works. Taking the 2015–19 average as a baseline of 2,165 deaths a year, we measured:

| Year | Deaths | vs 2015–19 baseline |
|---|---:|---:|
| 2019 | 2,134 | −1.4% |
| **2020** | **2,968** | **+37.1%** |
| 2021 | 2,553 | +17.9% |
| 2022 | 2,496 | +15.3% |
| 2023 | 2,263 | +4.5% |

A city of roughly 200,000 people buried a third again as many of its residents in 2020 as it
normally would. That is what the dataset is for, and it delivers it in four columns to anyone who
asks.

The comune understood this at the time. In March 2021 it published a second dataset,
*Decessi nel Comune di Brescia aggiornato al 20 marzo 2021*, whose description states the total
deaths since 1979 and the resident population at 31 December 2019 **so that excess mortality could be
quantified**. A third followed in July 2021. Somebody in Brescia sat down during the emergency and
deliberately built the public a way to check the toll for themselves. That deserves saying plainly,
and it is to the comune's credit.

## What happened next

All three datasets were last touched on **10 April 2024**. All three still declare their update
frequency as `Giornaliera` — daily.

The emergency produced exactly the right instinct and none of the durable process. There is no
successor, no monthly series, no continuation. The file that a city built to count its own dead
during the worst mortality event in its modern history now sits 852 days stale under a label
claiming it refreshes every day.

It is not that this is hard. Twenty-nine comuni across Lombardia publish the identical *Elenco
Decessi* template. Eleven have updated within the past year, and several within the past fortnight —
Gonzaga, Martignana, Castelbelforte, Bozzolo, Busto Arsizio. Small municipalities with a tiny
fraction of Brescia's traffic are keeping the same four columns current. The template works. The
pipeline exists. Brescia's stopped.

That is the loss. A pandemic is the moment when the case for maintained public mortality data is
easiest to make and hardest to argue with, and the institutional answer should have been a standing
series that outlives the crisis. What exists instead is three frozen snapshots and a false cadence
label, on the most consulted dataset in the region.

## What is still wrong with the file itself

**Zero of four columns are documented.** On a four-column file that sounds survivable and is not.
`occorrenze` is the count, and nothing states whether it counts deaths *occurring* in Brescia or
deaths *of Brescia residents* wherever they happened. Those give different denominators and a
different excess mortality figure. Every number in the table above rests on an assumption the file
declines to confirm.

**The title still misleads.** *Elenco Decessi* — list of deaths — implies a register, one row per
death. This is an aggregate frequency table, and 833 rows cannot be a list of 45 years of deaths in
a city this size.

**The resolution cannot see the thing it documented.** Brescia's catastrophe happened across a few
weeks in spring 2020. An annual total shows +37.1% for the year and cannot show March. The sibling
datasets were built precisely because someone wanted a finer cut, and they were not sustained
either.

## Working with it

Establish what `occorrenze` counts before computing any rate; ask the comune, because the file will
not say.

Use 2015–19 as your baseline and exclude 2024, which is a partial year (585 deaths against a full-year
norm above 2,000). Read `data_updated_at`, never the cadence field.

If you need this series maintained, the other twenty-nine comuni publishing the same template are the
argument to take to Brescia.

## The call

**Grade C+**, revised up from 5.2 after we tested the series properly and understood what it is for.
Completeness rises because a 45-year annual mortality series broken down by sex and citizenship,
which demonstrably measures a pandemic, is a more substantial thing than we first credited.

Everything else stands, and the pandemic context makes the failures sharper rather than softer. A
city built this to let its public count the dead, and then let it lapse under a label that says it
updates daily — while its neighbours keep the same file current. Four sentences of documentation and
a working refresh would make it what it briefly was.
