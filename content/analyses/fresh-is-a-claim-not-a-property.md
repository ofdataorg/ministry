---
title: "Fresh Is a Claim, Not a Property"
date: 2026-06-18
author: "Ministry desk"
description: "Update dates measure when a file changed, not when reality was observed. The gap between those two moments is where most bad analysis lives."
domains: ["Governance"]
regions: ["Global"]
toc: true
---

Almost every data portal shows an update date. Almost none of them show the thing you actually need,
which is the date the world being described was observed. The distance between those two timestamps
is the single most under-reported property in open data, and it routinely runs to years.

## Four clocks, not one

Any dataset has at least four:

1. **Reference period** — when the phenomenon happened.
2. **Collection date** — when it was observed or recorded.
3. **Publication date** — when it was first released.
4. **File modification date** — when the bytes last changed.

Portals overwhelmingly display the fourth. It is the least informative of the four and the easiest
to generate. A file re-exported with a new column header, or migrated between storage systems, gets
a fresh timestamp and looks maintained. Nothing about the world it describes has moved.

## The failure modes we keep hitting

**The dormant catalogue entry.** The
[Global Power Plant Database](/evaluations/global-power-plant-database/) has not shipped since
v1.3.0 in June 2021 — and it is honest about that, which is why we could score it fairly. Many
datasets in the same condition are not, and a live-looking page implies a maintenance intent that
ended years ago. On [HDX](/evaluations/humanitarian-data-exchange/), a maintained boundary file and
an abandoned 2017 assessment are presented identically.

**The averaged window read as a point.** The
[ACS 5-year estimates](/evaluations/american-community-survey/) pool sixty months of sample. They
are not "2024 data" and the Census Bureau says so repeatedly and clearly. They are still cited as
current-year figures every week, in charts that would not survive the caption "average conditions,
2020–2024".

**Inherited cadence.** Aggregators like [NDAP](/evaluations/india-ndap/) take their freshness from
whichever ministry contributed each dataset. The platform is current. Individual holdings range from
months to years old, with no consistent signal telling you which regime you are in. Users read the
platform's activity as the dataset's activity.

**The provisional file that moves.** Vital statistics systems publish preliminary counts that are
revised for years. [DATASUS](/evaluations/datasus-sim-mortality/) consolidates annually and
provisional figures shift materially. Analysis published on the preliminary file becomes wrong
quietly, after the fact, with no notification to anyone who cited it.

## The fix is metadata, not engineering

Publishers do not need faster pipelines to solve most of this. They need to publish three things
they already know:

- **The reference period**, explicitly, distinct from the release date.
- **The intended cadence** — and, when a dataset is no longer maintained, a plain statement saying
  so. "This dataset is no longer updated" is a service to every future user, not an admission of
  failure.
- **Provisional status**, marked in the data, with the expected revision horizon.

That is a metadata change. It costs a schema field and a sentence.

## How we score it

Our timeliness axis rates the gap between reference period and availability, plus whether cadence is
documented and honoured — not how recently the file changed. A dataset published annually, on
schedule, with a clearly stated six-month lag scores well. A dataset with a fresh modification
timestamp and no statement of what period it describes does not, regardless of how live the page
looks.

If you take one operational habit from this piece: before using any dataset, write down what period
it actually describes. If you cannot find that out from the documentation in five minutes, treat
that as a finding about the dataset, and record it.
