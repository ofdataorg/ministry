---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true

# Filing
publishers: ["Publishing body"]
regions: ["Global"]          # Global, Africa, Asia, Europe, North America, South America, Oceania
domains: ["Domain"]          # Climate, Health, Mobility, Economy, Biodiversity, Population...
licenses: ["CC BY 4.0"]

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
