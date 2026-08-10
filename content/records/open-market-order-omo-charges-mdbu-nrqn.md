---
title: "Open Market Order (OMO) Charges"
date: 2026-08-10
snapshot: 2026-08-10
portal: "NYC Open Data"
portal_ref: "/evaluations/nyc-open-data/"
place: "New York City"
dataset_id: "mdbu-nrqn"
source: "https://data.cityofnewyork.us/d/mdbu-nrqn"
category: "Housing & Development"
license: ""
declared_cadence: "Daily"
last_update: 2026-08-09
age_days: 0
cadence_kept: "yes"
condition: "attention"
measured:
  http: 200
  secs: 0.7
  rows: 200
  columns: 32
  null_mean: 0.1377
  cols_empty: 2
  cols_mistyped: 8
  cols_documented: 23
  dup_rows: 0
columns:
  - f: "omoid"
    type: "Number"
    empty: 0.0
    uniq: 200
    doc: true
  - f: "omonumber"
    type: "Text"
    empty: 0.0
    uniq: 200
    doc: true
  - f: "buildingid"
    type: "Number"
    empty: 0.0
    uniq: 192
    doc: true
  - f: "boro_id"
    type: "Number"
    empty: 0.0
    uniq: 5
    doc: true
  - f: "boro"
    type: "Text"
    empty: 0.0
    uniq: 5
    doc: true
  - f: "housenumber"
    type: "Text"
    empty: 0.0
    uniq: 188
    doc: true
  - f: "streetname"
    type: "Text"
    empty: 0.0
    uniq: 163
    doc: true
  - f: "apartment"
    type: "Text"
    empty: 0.325
    uniq: 93
    doc: false
  - f: "zip"
    type: "Text"
    empty: 0.005
    uniq: 84
    doc: true
    mistyped: true
  - f: "block"
    type: "Number"
    empty: 0.0
    uniq: 183
    doc: true
  - f: "lot"
    type: "Number"
    empty: 0.0
    uniq: 90
    doc: true
  - f: "lifecycle"
    type: "Text"
    empty: 0.0
    uniq: 1
    doc: true
  - f: "worktypegeneral"
    type: "Text"
    empty: 0.0
    uniq: 9
    doc: true
  - f: "omostatusreason"
    type: "Text"
    empty: 0.02
    uniq: 12
    doc: true
  - f: "omoawardamount"
    type: "Number"
    empty: 0.0
    uniq: 126
    doc: true
  - f: "omocreatedate"
    type: "Calendar date"
    empty: 0.0
    uniq: 145
    doc: true
  - f: "netchangeorders"
    type: "Number"
    empty: 0.0
    uniq: 1
    doc: true
  - f: "omoawarddate"
    type: "Calendar date"
    empty: 0.04
    uniq: 93
    doc: true
  - f: "isaep"
    type: "Text"
    empty: 0.945
    uniq: 1
    doc: true
  - f: "iscommercialdemolition"
    type: "Text"
    empty: 0.99
    uniq: 1
    doc: true
  - f: "servicechargeflag"
    type: "Text"
    empty: 0.0
    uniq: 2
    doc: true
  - f: "femaeventid"
    type: "Number"
    empty: 1.0
    uniq: 0
    doc: true
  - f: "femaevent"
    type: "Text"
    empty: 1.0
    uniq: 0
    doc: true
  - f: "omodescription"
    type: "Text"
    empty: 0.0
    uniq: 176
    doc: true
  - f: "latitude"
    type: "Text"
    empty: 0.01
    uniq: 190
    doc: false
    mistyped: true
  - f: "longitude"
    type: "Text"
    empty: 0.01
    uniq: 190
    doc: false
    mistyped: true
  - f: "community_board"
    type: "Text"
    empty: 0.01
    uniq: 17
    doc: false
    mistyped: true
  - f: "council_district"
    type: "Text"
    empty: 0.01
    uniq: 40
    doc: false
    mistyped: true
  - f: "census_tract"
    type: "Text"
    empty: 0.01
    uniq: 153
    doc: false
    mistyped: true
  - f: "bin"
    type: "Text"
    empty: 0.01
    uniq: 190
    doc: false
    mistyped: true
  - f: "bbl"
    type: "Text"
    empty: 0.01
    uniq: 190
    doc: false
    mistyped: true
  - f: "nta"
    type: "Text"
    empty: 0.01
    uniq: 111
    doc: false
---
