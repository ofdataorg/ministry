---
title: "NYC Open Market Order (OMO) Charges"
date: 2026-08-10
publishers: ["NYC Department of Housing Preservation and Development"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Housing", "Governance"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/mdbu-nrqn"
version: "Rolling feed — 511,110 rows at snapshot"
snapshot: 2026-08-10
temporal: "2013 to present"
updated: "9 August 2026"
cadence: "Declares Daily, automated, and keeps it"
formats: ["CSV", "JSON", "GeoJSON", "RDF", "TSV"]
size: "511,110 rows, 32 columns"
access: "Open API and bulk download, no registration"

verdict: "The city bills a landlord for a repair it had to make itself, and publishes the invoice daily."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 9
  documentation: 6
  accessibility: 9
  licensing: 3
  interoperability: 7

strengths:
  - "A genuine enforcement trail: every emergency repair the city carried out on a private building and charged back to the owner, at property level."
  - "23 of 32 columns documented — above the portal average, and the documented ones are the ones that matter."
  - "Daily and automated, with BBL, block, lot, community board, council district and census tract all present for joining."
weaknesses:
  - "The nine undocumented columns include `femaevent` and `femaeventid`, which are the only route to separating disaster-driven work from routine enforcement."
  - "`lifecycle` and `netchangeorders` carry the state of an order without a stated vocabulary, so reconstructing an order's history means inferring the state machine."
  - "No licence, in common with 97.4% of the [portal](/evaluations/nyc-open-data/)."

bestfor:
  - "Housing enforcement research — which buildings the city has had to repair itself"
  - "Property-level landlord accountability work, joined via BBL"
  - "Tracking the cost of the Emergency Repair Program over time"
avoidfor:
  - "Assuming a charge equals a completed repair without reading `lifecycle`"
  - "Separating storm-response work from routine enforcement without decoding the FEMA fields"
---

## What it is

Work orders created under New York's Emergency Repair Program, Alternative Enforcement Program and
demolition programmes, together with the charges assessed against the property afterwards. When a
landlord fails to fix something the Housing Maintenance Code requires, the city can do the work and
bill them. This is that ledger: 511,110 rows, 32 columns, updated daily since 2013.

It is a more interesting dataset than its title suggests. Emergency repair charges are one of the
few public, property-level records of landlords failing their obligations badly enough that a
municipality intervened.

## How it holds up

**Timeliness and access are straightforwardly good.** Declared Daily, automated, current the day
before we pulled it. The geography is complete — `bbl`, `block`, `lot`, `boro`, `community_board`,
`council_district`, `census_tract` — so it joins to housing, demographic and complaint data without
any preparation.

**Documentation is above average and unevenly distributed.** 23 of 32 columns carry a description,
which comfortably beats the portal's 31.1% and reflects real effort. The gaps are the frustrating
part, because of which columns they are.

`femaevent` and `femaeventid` are undocumented. Those fields presumably tie work orders to declared
federal disaster events, which is the only way to separate storm-response work from routine
enforcement — and separating them matters, because a spike after a hurricane is not a spike in
landlord neglect. Without a vocabulary or a link to the FEMA event register, a researcher has to
reverse-engineer the codes.

`lifecycle` and `netchangeorders` are the other significant gaps. An order moves through states and
accrues change orders; the columns record where it got to, without saying what the states are. So
the difference between an order raised, an order completed and an order billed is inferable but not
stated, and anyone summing charges without understanding it risks counting work that never happened.

## Working with it

Join on `bbl` and treat `omoid` as the row key, not `omonumber` — the latter looks like a
human-facing reference and is not obviously unique.

Read `lifecycle` before aggregating anything financial. Establish empirically which values represent
a completed, billed order, and state your assumption when you publish, because the dataset will not
state it for you.

If your question is about neglect rather than weather, filter on the FEMA fields first and satisfy
yourself you understand what they mean.

## The call

**Grade B.** A properly maintained, well-joined, genuinely useful enforcement dataset that documents
two thirds of itself. It sits a clear grade below where it could be for the sake of nine column
descriptions — and specifically for the sake of the two or three that decide whether an analyst
counts the right rows.
