---
title: "NYC Open Data"
date: 2026-08-10
publishers: ["City of New York"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Governance", "Mobility", "Housing"]
licenses: ["None stated"]

source: "https://opendata.cityofnewyork.us/"
version: "Catalogue as at 10 August 2026 — 3,014 assets, 2,396 datasets; 300 sampled and downloaded"
snapshot: 2026-08-10
temporal: "Varies by dataset; many series run from the 2000s"
updated: "Continuously for automated feeds"
cadence: "Declared on 100% of datasets; 65.9% of testable promises kept"
formats: ["CSV", "JSON", "GeoJSON", "RDF", "TSV"]
size: "2,396 datasets, ~57,000 columns"
access: "Open API and bulk download, no registration"

verdict: "The best-run municipal data operation in the world, publishing three thousand datasets that nobody has said you are allowed to use."
reviewer: "Ministry desk"

history:
  - date: 2026-08-10
    version: "Catalogue as at 10 August 2026 — 3,014 assets, 2,396 datasets"
    note: "First scoring, from catalogue metadata and two sample downloads. Superseded the same day by [an audit of 300 randomly sampled datasets](/analyses/we-opened-six-hundred-datasets/), which found 12.3% of columns entirely empty and 20.6% of Text-declared columns holding only numbers — evidence not visible from the catalogue. Completeness and interoperability revised down."
    scores: { completeness: 8, timeliness: 6, documentation: 6, accessibility: 9, licensing: 3, interoperability: 8 }

scores:
  completeness: 7
  timeliness: 6
  documentation: 6
  accessibility: 9
  licensing: 3
  interoperability: 7

strengths:
  - "**Every single dataset declares an update frequency** — 2,396 out of 2,396. No other catalogue we have measured manages that."
  - "971 datasets are honestly marked `Historical data` rather than left to look live, and an `Update_Automation` flag says whether a human or a machine keeps each one current."
  - "The SODA API is excellent: no key required, 500 rows of 311 data in under a second, and CSV, JSON, GeoJSON, RDF and TSV off the same endpoint."
weaknesses:
  - "**2,935 of 3,014 assets — 97.4% — state no licence at all**, and the portal grants none either. The flagship 311 dataset is among them."
  - "Only 65.9% of testable cadence promises are kept. Annual series manage 53.2%, six-monthly 55.6%, weekly 57.9%."
  - "Median dataset was last updated 1,039 days ago and 48% have not moved in over four years, even though the live ones are genuinely live."
  - "In a 300-dataset sample, 12.3% of columns came back entirely empty — 333 of 464 in the 2020 DOE Middle School Directory alone — and 20.6% of columns declared `Text` hold only numbers."

bestfor:
  - "City operations, 311, transport and buildings data at real scale"
  - "Anything that needs a working API rather than a download button"
  - "A model of how to declare update cadence — every publisher should copy this part"
avoidfor:
  - "Commercial products, until someone at the City writes a licence"
  - "Assuming catalogue membership implies a maintained dataset"
  - "Counting 3,014 as a dataset total — 143 of those entries are links to other websites"
---

## What it is

The City of New York's open data portal: 3,014 catalogue assets, of which 2,396 are actual
datasets, running on Socrata. It exists because of a law — Local Law 11 of 2012 obliges city
agencies to publish their data — and that mandate shows in the breadth. City Government, Education,
Transportation, Environment, Housing, Social Services, Public Safety: 906 datasets in the largest
category alone. All 3,014 assets are official; there is no community-contributed clutter.

Figures here were measured against the Socrata Discovery API on 10 August 2026.

## How it holds up

**Start with the thing nobody else does.** Every one of the 2,396 datasets declares an update
frequency. Not most. All of them. After finding that
[Bologna](/evaluations/comune-di-bologna-open-data/) hid its cadence in a machine-readable layer and
left the human-facing field empty, seeing a portal state it universally and put it on the page is a
genuine pleasure.

It goes further. An `Update_Automation` field records whether each dataset is refreshed by a
pipeline or by a person — 610 automated, 2,307 not — which is exactly the distinction that predicts
whether a dataset will rot. And 971 datasets are labelled `Historical data`: a closed archive,
honestly marked, not left to imply currency it does not have. This is the metadata discipline we
have been asking publishers for.

**Then look at whether the promises hold.** Of the 1,053 datasets making a testable commitment,
694 are inside a generous window — **65.9%**:

| Declared | Datasets | Median age | Inside window |
|---|---:|---:|---:|
| Daily | 129 | same day | 72.9% |
| Weekly | 57 | 6 days | 57.9% |
| Monthly | 261 | 10 days | 77.8% |
| Quarterly | 128 | 75 days | 84.4% |
| Every 6 months | 72 | 156 days | 55.6% |
| Annually | 406 | 346 days | 53.2% |
| Historical data | 971 | 7.1 years | not applicable |
| As needed | 267 | 3.3 years | not testable |

Two thirds is a pass, not a distinction. The annual series are the weak point — over 400 datasets
declare a yearly cadence and barely half are current against it. And "As needed", used by 267
datasets sitting at a median of over three years, is the same non-promise we criticised elsewhere:
it cannot be broken because it does not say anything.

Across the whole catalogue the median dataset was last updated 1,039 days ago and 48% have not
moved in over four years. The live ones are properly live — 311 had updated the day we looked — but
the distribution is bimodal and the frozen half is large.

**And then there is the licence, which is the reason this evaluation is not an A.**

**2,935 of 3,014 assets — 97.4% — carry no licence statement whatsoever.** Fifty-nine are CC BY
4.0, nineteen are marked Public Domain, one is ODbL. The other 97% are silent. That includes 311
Service Requests, the most consulted dataset the city publishes.

The portal's own Terms of Use do not fill the gap. They say, in full, that by accessing the data
you agree to the Terms of Use of nyc.gov and its privacy policy — a website agreement, not a data
licence. No permission to redistribute is granted. No permission for commercial use is granted. No
open licence is named. What the terms do supply is a disclaimer of warranty and a statement that
agencies remain the authoritative source.

It is tempting to assume this is all public domain. In the United States that assumption is safe
for *federal* works, which are denied copyright by statute. It is not safe for a *municipality*. A
city can hold copyright in its works, and New York has not said it does not. So the actual position
is that the largest municipal open data programme in the world publishes three thousand datasets
whose reuse terms are undefined, and every serious commercial user has to decide privately whether
to risk it.

This is the failure mode we set out in [The Licence Is the Dataset](/analyses/the-licence-is-the-dataset/)
— unstated terms — at the largest scale we have encountered. It costs six points.

**Documentation is respectable.** 17,740 of roughly 57,000 columns carry a description — 31.1%,
which is above the median of the catalogues we have measured — and many datasets attach a data
dictionary. 17.9% of assets have a description under 80 characters.

One padding complaint: 143 catalogue entries are of type `href`. They are links to other websites —
Citi Bike System Data, Citywide Crime Statistics — counted as catalogue assets. They are useful
signposts and they are not datasets, and a headline count of 3,014 quietly includes them.

## What 300 downloads showed

Catalogue metadata is where the scoring above starts, not where it ends. We drew a random sample of
300 official datasets and pulled 200 rows from each; the full method and cross-portal comparison is
in [We Opened Six Hundred Datasets](/analyses/we-opened-six-hundred-datasets/).

The access story held up completely: **299 of 300 downloaded**, none returned an empty file, median
response 0.66 seconds. For a catalogue this size that is a genuinely strong result and it confirms
the accessibility score.

Two findings pulled the other way. **12.3% of all columns in the sample were entirely empty** —
996 of 8,067 — and 18.1% of datasets carried at least one. The concentration is extreme: the 2020
DOE Middle School Directory publishes 464 columns of which **333 contain nothing at all**, and 88%
of its cells are blank. These are wide survey instruments exported whole, with every unasked
question preserved as a column. The rows that exist are fine; the schema is several times larger
than the data, and a user has to discover that by opening it.

And **20.6% of columns declared `Text` contain only numbers** — a fifth of the numeric columns
arrive as strings that will not sum until cast. Lombardia, on the same platform, produced the
identical figure to the decimal, which tells you this is the ingest default rather than anything
New York decided. It is still work the consumer pays for.

Neither finding is visible from the catalogue. Both moved the grade.

## Working with it

Use the SODA API, not the download button. `https://data.cityofnewyork.us/resource/{id}.csv?$limit=`
works without a key; register an app token if you are going to hammer it, since anonymous requests
share a throttling pool.

Read `Update_Update-Frequency` and `Update_Automation` before you build on anything. Between them
they tell you more about whether a dataset will still be there next quarter than any other metadata
on the portal.

On licensing, get a decision in writing before you ship a commercial product on this data. It is
almost certainly fine in practice and that is not the same as being fine.

## The call

**Grade B−**, revised down from B after the sampling. Operationally this is close to the best municipal data programme in the world: the
scale is real, the API is excellent, and the cadence metadata is the most complete we have measured
anywhere. The engineering deserves an A−.

What holds it back is a single omission that a lawyer could fix in an afternoon. Attach CC0 or
CC BY 4.0 to the catalogue, as Lombardia has, and this becomes one of the highest-scoring entries on
this site. Until then the City has built a magnificent library and forgotten to unlock the door.
