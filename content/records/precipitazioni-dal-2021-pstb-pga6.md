---
title: "Precipitazioni dal 2021"
date: 2026-08-10
snapshot: 2026-08-10
portal: "Open Data Regione Lombardia"
portal_ref: "/evaluations/dati-lombardia/"
place: "Lombardia"
dataset_id: "pstb-pga6"
source: "https://www.dati.lombardia.it/d/pstb-pga6"
category: "Ambiente"
license: "Creative Commons 1.0 Universal (Public Domain Dedication)"
declared_cadence: "semestrale"
last_update: 2026-03-06
age_days: 156
cadence_kept: "yes"
condition: "serviceable"
measured:
  http: 200
  secs: 0.15
  rows: 200
  columns: 4
  null_mean: 0.0
  cols_empty: 0
  cols_mistyped: 0
  cols_documented: 4
  dup_rows: 0
columns:
  - f: "idsensore"
    type: "Text"
    empty: 0.0
    uniq: 1
    doc: true
  - f: "data"
    type: "Calendar date"
    empty: 0.0
    uniq: 200
    doc: true
  - f: "valore"
    type: "Number"
    empty: 0.0
    uniq: 6
    doc: true
  - f: "stato"
    type: "Text"
    empty: 0.0
    uniq: 1
    doc: true
---
