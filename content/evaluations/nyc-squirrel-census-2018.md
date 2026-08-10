---
title: "2018 Central Park Squirrel Census"
date: 2026-08-10
publishers: ["The Squirrel Census", "NYC Open Data"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Biodiversity", "Society"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/vfnx-vebw"
version: "2018 census — 3,023 sightings, published October 2019"
snapshot: 2026-08-10
temporal: "6–20 October 2018"
updated: "18 October 2019"
cadence: "Declares Historical data — a completed one-off count"
formats: ["CSV", "JSON", "GeoJSON", "RDF", "TSV"]
size: "3,023 squirrel sightings, 36 columns"
access: "Open API and bulk download, no registration"

verdict: "Three thousand squirrels, counted by volunteers over two weeks, documented better than most of the city's statutory data."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 8
  documentation: 8
  accessibility: 9
  licensing: 3
  interoperability: 7

strengths:
  - "30 of 36 columns documented — better coverage than the city achieves on its own permitting and housing data."
  - "**`Historical data` is exactly the right label** and it is used correctly: a fortnight-long census in 2018 is finished, and the file says so instead of implying maintenance."
  - "Rigorous field design for a volunteer project: hectare grid, shift, sighter above or below ground, and separate behavioural columns for running, chasing, climbing, foraging, kuks, quaas, moans, tail flags and tail twitches."
weaknesses:
  - "One park, one fortnight, one year — an excellent sample of a very small thing, and its popularity invites over-reading."
  - "No licence, on a dataset produced by an outside project and hosted by the city, which makes the ambiguity worse rather than better."
  - "Behavioural columns are booleans recorded by different volunteers, so observer variation is baked in and undocumented."

bestfor:
  - "Teaching data literacy — it is small, clean, documented and genuinely fun"
  - "Urban ecology methods, as a worked example of volunteer survey design"
  - "Spatial exercises: it ships coordinates and a hectare grid"
avoidfor:
  - "Squirrel population estimates beyond Central Park in October 2018"
  - "Behavioural inference without accounting for who was doing the observing"
---

## What it is

Three thousand and twenty-three squirrel sightings recorded in Central Park between 6 and 20 October
2018 by volunteers of The Squirrel Census, a self-described science, design and storytelling project.
Each row is one Eastern grey squirrel: where it was, on a hectare grid and in coordinates, whether it
was above ground, its primary and highlight fur colour, and what it was doing — running, chasing,
climbing, eating, foraging — along with the noises it made.

It is one of the most-viewed datasets New York publishes, with over 300,000 page views, and it is
here on merit rather than novelty.

## How it holds up

**The documentation embarrasses the city's own data.** 30 of 36 columns carry a description. The
[DOB NOW permits feed](/evaluations/nyc-dob-now-approved-permits/), a statutory dataset from a city
agency, documents none of its 46. A volunteer squirrel-counting project did the work that the
Department of Buildings did not.

**The cadence label is correct, and that matters more than it sounds.** It declares
`Historical data`. A census that ran for a fortnight in 2018 is complete; it will never update; and
saying so is the honest and useful thing. Set against the 444 Lombardia datasets that
[declare themselves prompt](/evaluations/dati-lombardia/) while sitting seven years untouched, this
is what a closed dataset should look like.

**The survey design is better than it needed to be.** The park is divided into a hectare grid, so
sightings are locatable to a defined cell rather than a guess. `shift` records morning or afternoon.
`above_ground_sighter` distinguishes the observer's vantage point. Behaviours are separate boolean
columns rather than a single free-text field, and the vocalisation columns — `kuks`, `quaas`,
`moans` — use the actual ethological terms for grey squirrel calls. Somebody read the literature.

**Its limits are the obvious ones and they are worth stating because of the popularity.** This is one
park, one fortnight, one year. It supports statements about squirrels observed in Central Park in
October 2018 and nothing wider. The behavioural columns were recorded by many different volunteers
with, presumably, varying thresholds for what counts as "foraging" — inter-observer variation that
is real, unavoidable in citizen science, and not quantified here.

**The licence gap is more awkward here than elsewhere.** Most unlicensed NYC datasets are at least
the city's own work. This one was produced by an external project and hosted by the city, so the
question of who holds rights and what a reuser may do has two possible answers instead of one, and
the portal supplies neither.

## Working with it

Use the hectare grid for spatial aggregation rather than raw coordinates; it is what the survey was
designed around. Treat each behavioural boolean as an observation of an observer as much as of a
squirrel.

If you are teaching with it — and many people do — it is a genuinely good file for the purpose:
small enough to read, clean enough to load, documented enough to interrogate, and interesting
enough that students actually look at it.

## The call

**Grade B.** Charming, rigorous, honestly labelled and well documented — a volunteer project that
published to a higher standard than several statutory datasets on the same portal. It is capped by
scope, which is inherent rather than a failing, and by the same missing licence that affects almost
everything on NYC Open Data, made murkier by the third-party provenance.
