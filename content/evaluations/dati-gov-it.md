---
title: "dati.gov.it — Italy's National Catalogue"
date: 2026-08-11
publishers: ["AgID — Agenzia per l'Italia Digitale"]
regions: ["Europe"]
place: "Italy"
places: ["European Union", "Italy"]
domains: ["Governance", "Geospatial"]
licenses: ["CC BY 4.0"]

source: "https://www.dati.gov.it/"
version: "Catalogue as at 11 August 2026 — 65,828 datasets; 3,000 sampled, 3,302 cross-checked, 120 links tested"
snapshot: 2026-08-11
temporal: "Varies by source catalogue"
updated: "Harvested continuously"
cadence: "Not declared per dataset; the harvest runs on its own schedule"
formats: ["CSV", "JSON", "XML", "RDF", "ZIP"]
size: "65,828 datasets from ~500 publishing bodies"
access: "Open CKAN API and bulk download, no registration"

verdict: "Every dataset in Italy in one place, every one of them stamped as modified this week — including the ones nobody has touched since 2012."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 3
  documentation: 5
  accessibility: 9
  licensing: 7
  interoperability: 6

strengths:
  - "**65,828 datasets from roughly 500 public bodies** — regions, ministries, comuni, INPS, the national geodata register — genuinely aggregated into one searchable catalogue with one API."
  - "A working, standard CKAN API with no key and no gate, so the whole catalogue is queryable and harvestable by anyone."
  - "86.5% of holdings are CC BY 4.0 and a further 5.7% CC0, giving Italy a coherent national licensing position that most federations lack."
weaknesses:
  - "**`metadata_modified` is the harvest timestamp, not the data's.** Median age across our sample: 2 days. Not one dataset in 3,000 appeared older than 30 days."
  - "We proved what that hides: of 2,432 Lombardia datasets matched to their source portal, **1,355 have not been touched in over four years — and the national catalogue stamps every single one of them as modified within the last 30 days.**"
  - "11.7% of resource links do not resolve — 8.3% return 404 or 410, 3.3% fail to connect at all."

bestfor:
  - "Discovering what Italian public data exists, and who publishes it"
  - "Cross-publisher search that no single regional portal can offer"
  - "Harvesting a national inventory — provided you read the right date field"
avoidfor:
  - "Judging whether a dataset is current from `metadata_modified`"
  - "Assuming a listed resource is downloadable"
  - "Sorting by recency in the default CKAN view"
---

## What it is

Italy's national open data catalogue, run by AgID: **65,828 datasets** harvested from roughly 500
public bodies. Regione Toscana contributes 12,426, Veneto 6,606, Marche 5,444, the national
geospatial register 4,076, the Ministry of Economy and Finance 3,714, Regione Lombardia 3,302,
Comune di Milano 2,599.

It is a harvester, not a publisher. Every record in our 3,000-dataset sample had
`dataset_is_local: false` — nothing originates here. That is the correct architecture for a national
catalogue, and it makes the question of what a national catalogue owes its users a specific one:
if you did not create the data, what exactly are you responsible for?

Figures measured against the CKAN API on 11 August 2026.

## How it holds up

**The aggregation itself is a real achievement.** One API, one query language, one place to find out
whether an Italian public body publishes something. 45,097 CSV resources, 15,166 JSON, 11,499 XML,
6,445 RDF. No registration, no key, no rate-limit theatre. For anyone who has tried to work across
Italian regional portals individually — each with its own platform, vocabulary and quirks — the
value of this is obvious and large.

**And then the clock, which is the reason this is not an A.**

Across our 3,000-dataset sample, the median `metadata_modified` was **2 days old**, and **100% of the
sample was under 30 days**. Not one dataset in three thousand appeared older than a month.

That is not because Italian public data is extraordinarily well maintained. It is because
`metadata_modified` records when the *harvester* last wrote the record, not when the *data* last
changed. Every harvest re-stamps everything.

We were able to prove this precisely, because we already hold the source figures. We evaluated
[Regione Lombardia's own portal](/evaluations/dati-lombardia/) last week and measured
`data_updated_at` for every dataset on it. Matching 2,432 of Lombardia's datasets to their entries
here by title:

| | National catalogue | Source portal |
|---|---:|---:|
| Median apparent age | **2 days** | **1,840 days** |
| Oldest | 149 days | 5,229 days |

**1,355 of those 2,432 datasets — 55.7% — have not been touched at source in over four years. The
national catalogue stamps 100% of them as modified within the last 30 days.**

The worst cases are almost comic. *Nuclei Operativi Alcologia* was last genuinely updated 5,229 days
ago — over fourteen years — and appears here as modified two days ago. *Elezioni Politiche Comunali
2008*, which we [evaluated separately](/evaluations/lombardia-elezioni-politiche-2008/) and which is
correctly labelled at source as never updating, is presented nationally as fresh this week.

**In fairness, the truth is preserved — it is just demoted.** The real modification date survives in
the `extras` array as `modified`, and it is accurate: median 1,996 days, agreeing with the source
portal's own date within 90 days in **80% of cases**. So dati.gov.it is not destroying the signal.
It is putting the harvest timestamp in the field every CKAN client reads by default and the truth in
a nested array most consumers never open. A field called `source_catalog_modified` sounds like it
should help and does not — it too is a harvest artefact, median 4 days.

This is the four-clocks problem from [Fresh Is a Claim, Not a Property](/analyses/fresh-is-a-claim-not-a-property/)
at national scale: four timestamps, and the one on top is the least informative.

**Link rot is the second harvester problem.** We tested 120 randomly sampled resource URLs.
88.3% resolved; **8.3% returned 404 or 410 and 3.3% could not be reached at all** — 11.7% broken
overall. Failures clustered heavily in one publisher, and several dead links were shortened Google
URLs and Google Sheets exports that have since expired, which is a publishing practice a national
catalogue is well placed to discourage and does not.

**Licensing is good with an avoidable wart.** 86.5% CC BY 4.0, 5.7% CC0 — a coherent national
position. But the same licence is recorded under at least four different `license_id` values across
the catalogue: the full Italian title used as an identifier, plus `cc-by`, `cc-by4` and
`CC-BY-4.0`. Any consumer filtering by licence has to know all four spellings or silently lose
records.

## Working with it

**Read `extras.modified`, never `metadata_modified`.** That single substitution is the difference
between a usable national inventory and a catalogue that claims 65,828 datasets were all updated
this week.

Check resources before you promise anyone a pipeline; roughly one link in nine is dead. Normalise
licence identifiers across at least four spellings.

Use it for discovery and then go to the source portal for the data. That is what a harvester is for,
and this one does the discovery part well.

## The call

**Grade B−.** As an aggregation this is genuinely valuable and technically sound: comprehensive
coverage, an open standard API, and a national licensing position most federal systems never
achieve.

It is held down by a freshness signal that is actively misleading in the default view. The
information needed to fix it is already in the record — the catalogue holds the true date and
publishes it one level down. Promoting `extras.modified` into `metadata_modified`, or simply
surfacing it in the interface, would turn the single worst thing about this portal into one of its
strengths, and would cost a schema change rather than a publishing programme.
