---
title: "New York City Employment Forecast"
date: 2026-08-10
snapshot: 2026-08-10
portal: "NYC Open Data"
portal_ref: "/evaluations/nyc-open-data/"
place: "New York City"
dataset_id: "nsk4-4pvs"
source: "https://data.cityofnewyork.us/d/nsk4-4pvs"
category: "City Government"
license: ""
declared_cadence: "This dataset is updated two times per year after publication of the Preliminary and Executive Budget, usually in January and April respectively."
last_update: 2026-05-15
age_days: 86
cadence_kept: "na"
condition: "attention"
measured:
  http: 200
  secs: 0.51
  rows: 200
  columns: 6
  null_mean: 0.1667
  cols_empty: 1
  cols_mistyped: 2
  cols_documented: 6
  dup_rows: 0
columns:
  - f: "pub_dt"
    type: "Text"
    empty: 0.0
    uniq: 5
    doc: true
    mistyped: true
  - f: "ref_yr"
    type: "Text"
    empty: 0.0
    uniq: 5
    doc: true
    mistyped: true
  - f: "ind"
    type: "Text"
    empty: 0.0
    uniq: 15
    doc: true
  - f: "unit"
    type: "Text"
    empty: 0.0
    uniq: 1
    doc: true
  - f: "value"
    type: "Number"
    empty: 0.0
    uniq: 184
    doc: true
  - f: "rev_rea"
    type: "Text"
    empty: 1.0
    uniq: 0
    doc: true
---
