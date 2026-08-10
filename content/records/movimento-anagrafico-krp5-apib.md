---
title: "Movimento Anagrafico"
date: 2026-08-10
snapshot: 2026-08-10
portal: "Open Data Regione Lombardia"
portal_ref: "/evaluations/dati-lombardia/"
place: "Lombardia"
dataset_id: "krp5-apib"
source: "https://www.dati.lombardia.it/d/krp5-apib"
category: "Statistica"
license: ""
declared_cadence: "Annuale"
last_update: 2024-01-17
age_days: 935
cadence_kept: "no"
condition: "attention"
measured:
  http: 200
  secs: 0.23
  rows: 200
  columns: 13
  null_mean: 0.0
  cols_empty: 0
  cols_mistyped: 1
  cols_documented: 13
  dup_rows: 0
columns:
  - f: "anno"
    type: "Text"
    empty: 0.0
    uniq: 1
    doc: true
  - f: "codice_istat_provincia"
    type: "Number"
    empty: 0.0
    uniq: 2
    doc: true
  - f: "provincia"
    type: "Text"
    empty: 0.0
    uniq: 2
    doc: true
  - f: "codice_istat_comune"
    type: "Text"
    empty: 0.0
    uniq: 200
    doc: true
    mistyped: true
  - f: "comune"
    type: "Text"
    empty: 0.0
    uniq: 200
    doc: true
  - f: "totale_nati"
    type: "Number"
    empty: 0.0
    uniq: 89
    doc: true
  - f: "totale_nati_femmine"
    type: "Number"
    empty: 0.0
    uniq: 62
    doc: true
  - f: "totale_morti"
    type: "Number"
    empty: 0.0
    uniq: 89
    doc: true
  - f: "totale_morti_femmine"
    type: "Number"
    empty: 0.0
    uniq: 62
    doc: true
  - f: "totale_iscritti_per_trasferimento"
    type: "Number"
    empty: 0.0
    uniq: 155
    doc: true
  - f: "totale_cancellati_per_trasferimento"
    type: "Number"
    empty: 0.0
    uniq: 147
    doc: true
  - f: "totale_residenti_al_31_12"
    type: "Number"
    empty: 0.0
    uniq: 200
    doc: true
  - f: "totale_residenti_al_31_12_femmine"
    type: "Number"
    empty: 0.0
    uniq: 196
    doc: true
---
