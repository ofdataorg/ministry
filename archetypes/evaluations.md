---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true

# Filing
publishers: ["Publishing body"]
regions: ["Global"]          # Global, Africa, Asia, Europe, North America, South America, Oceania
domains: ["Domain"]          # Climate, Health, Mobility, Economy, Biodiversity, Population...
licenses: ["CC BY 4.0"]

# What was evaluated, and when.
# `snapshot` is the date the data was actually pulled — leave it out rather
# than inventing one, and the page will say the evaluation is unverified.
version: "v0.0.0 (Month YYYY)"   # or a descriptor if the publisher does not version
snapshot: YYYY-MM-DD

# Spec sheet
source: "https://example.org/dataset"
temporal: "1990–present"
updated: "Month YYYY"
cadence: "Annual"
formats: ["CSV", "Parquet"]
size: "0 rows / 0 GB"
access: "Direct download, no registration"

# The call
verdict: "One sentence a busy reader can quote."
reviewer: "Your name"

scores:
  completeness: 5
  timeliness: 5
  documentation: 5
  accessibility: 5
  licensing: 5
  interoperability: 5

# Prior scorings, if this dataset has been re-evaluated. Grades are
# recomputed from these axes, never written down, so a past grade is
# derived exactly like the present one.
# history:
#   - date: YYYY-MM-DD
#     version: "the version scored then"
#     note: "What changed between then and now."
#     scores: { completeness: 5, timeliness: 5, documentation: 5,
#               accessibility: 5, licensing: 5, interoperability: 5 }

strengths:
  - "What genuinely holds up."
weaknesses:
  - "What falls down under load."

bestfor:
  - "The question this dataset answers well."
avoidfor:
  - "The question people wrongly ask of it."
---

## What it is

## How it holds up

## Working with it

## The call
