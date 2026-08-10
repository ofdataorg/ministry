---
title: "NYC Motor Vehicle Collisions — Person"
date: 2026-08-10
publishers: ["NYPD"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Mobility", "Health"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/f55k-p6yu"
version: "Rolling feed — 5,984,110 rows at snapshot; pipeline broken since June"
snapshot: 2026-08-10
temporal: "2012 to June 2026"
updated: "15 June 2026"
cadence: "Declares Daily; currently not updating, and says so"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "5,984,110 person records, 21 columns"
access: "Open API and bulk download, no registration"

verdict: "Six million people involved in New York crashes, every column documented — and a pipeline that has been broken for two months in a dataset still labelled Daily."
reviewer: "Ministry desk"

scores:
  completeness: 8
  timeliness: 5
  documentation: 9
  accessibility: 9
  licensing: 3
  interoperability: 8

strengths:
  - "**All 21 columns documented**, on a person-level casualty file — injury, bodily part, ejection, safety equipment, contributing factors and pedestrian action are all explained."
  - "`collision_id` and `vehicle_id` join cleanly to the sibling crash and vehicle tables, so the three together reconstruct an incident completely."
  - "The publisher discloses the outage in plain language at the top of the description rather than letting the file quietly go stale."
weaknesses:
  - "**The pipeline has been broken since 15 June** and the machine-readable cadence still reads `Daily`. A consumer reading metadata rather than prose sees a healthy daily feed."
  - "`person_id` is a UUID that changes between refreshes in the sibling tables, so it is not a durable key across pulls."
  - "No licence, in common with 97.4% of the [portal](/evaluations/nyc-open-data/)."

bestfor:
  - "Vision Zero and road safety research at person level"
  - "Injury outcome analysis by road user type"
  - "Joining casualties to crash circumstances via `collision_id`"
avoidfor:
  - "Anything needing collisions after mid-June 2026 until the feed resumes"
  - "Treating `person_id` as a stable identifier across downloads"
---

## What it is

One row per person involved in a reported motor vehicle collision in New York City: 5,984,110
records across 21 columns. Whether they were a driver, passenger, cyclist or pedestrian; their age
and sex; what they were doing; whether they were ejected; what part of the body was injured; what the
police recorded as contributing. It is the person-level table of a three-part family — crashes,
vehicles, persons — linked by `collision_id`.

For road safety research this is close to the richest municipal casualty dataset in existence, and
the NYPD documents **all 21 columns**.

## How it holds up

**On substance and documentation it is excellent.** Full column coverage on a file where the fields
carry real analytical weight — `bodily_injury`, `ejection`, `safety_equipment`, `ped_action`,
`ped_location`, `contributing_factor_1` and `_2`. Person-level data with those attributes is what
makes it possible to ask whether a countermeasure reduced severity rather than just counts.

The three-table structure is the right design. Persons join to vehicles join to crashes, so a
researcher can move between "how many people were hurt" and "what kind of vehicle hit them at what
kind of junction" without leaving the portal.

**And the feed is broken.** The description opens with a note, in bold: the dataset is temporarily
not updating while its automated update process is being fixed, with the fix expected during August.
The most recent record is dated 15 June 2026 — nearly two months before we looked.

We want to give real credit for that disclosure. A publisher who notices a broken pipeline and says
so at the top of the page is doing something most do not, and it is the difference between a
dataset that is late and a dataset that is lying.

But the disclosure is in prose only. The machine-readable metadata still declares `Daily` with
`Update_Automation: Yes`. Anyone consuming this portal programmatically — which is the audience the
excellent [cadence metadata](/evaluations/nyc-open-data/) exists to serve — sees a healthy daily feed
and no indication of an outage. New York's cadence declarations are the best we have measured; this
is the case that shows the declaration needs a status alongside it, not just a frequency.

The practical consequence for anyone modelling road safety this summer is a two-month hole that
looks like a fall in collisions.

## Working with it

Pull the crashes and vehicles tables alongside this one and join on `collision_id`; on its own the
person table cannot tell you where anything happened.

Do not use `person_id` as a durable key across separate downloads — it is a UUID that has been
observed to change on refresh. `unique_id` is the stable row identifier.

Check the maximum `crash_date` in your extract before drawing a trend. Right now it will be June.

## The call

**Grade B.** The data and the documentation are close to best-in-class for municipal casualty
statistics, and the honesty about the outage deserves acknowledgement rather than punishment.

Timeliness still scores a 5, because a road safety dataset two months in arrears is two months in
arrears however gracefully it is admitted — and because the admission never reached the metadata,
where most automated consumers would look.
