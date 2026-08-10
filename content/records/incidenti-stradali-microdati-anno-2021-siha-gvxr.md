---
title: "Incidenti Stradali - Microdati - Anno 2021"
date: 2026-08-10
snapshot: 2026-08-10
portal: "Open Data Regione Lombardia"
portal_ref: "/evaluations/dati-lombardia/"
place: "Lombardia"
dataset_id: "siha-gvxr"
source: "https://www.dati.lombardia.it/d/siha-gvxr"
category: "Sicurezza"
license: "Creative Commons Attribution 4.0 International"
declared_cadence: "microdati incidenti stradali"
last_update: 2025-01-20
age_days: 566
cadence_kept: "na"
condition: "serviceable"
measured:
  http: 200
  secs: 0.35
  rows: 200
  columns: 22
  null_mean: 0.1366
  cols_empty: 0
  cols_mistyped: 1
  cols_documented: 0
  dup_rows: 0
columns:
  - f: "codice_istat_comune"
    type: "Text"
    empty: 0.0
    uniq: 21
    doc: false
    mistyped: true
  - f: "denominazione_comune"
    type: "Text"
    empty: 0.0
    uniq: 21
    doc: false
  - f: "provincia"
    type: "Text"
    empty: 0.0
    uniq: 1
    doc: false
  - f: "anno"
    type: "Text"
    empty: 0.0
    uniq: 1
    doc: false
  - f: "mese"
    type: "Number"
    empty: 0.0
    uniq: 12
    doc: false
  - f: "localizzazione_incidente"
    type: "Number"
    empty: 0.0
    uniq: 7
    doc: false
  - f: "denominazione_strada"
    type: "Text"
    empty: 0.57
    uniq: 23
    doc: false
  - f: "tipo_strada"
    type: "Number"
    empty: 0.0
    uniq: 4
    doc: false
  - f: "intersezione_nonintersezione"
    type: "Number"
    empty: 0.0
    uniq: 9
    doc: false
  - f: "natura_incidente"
    type: "Number"
    empty: 0.0
    uniq: 11
    doc: false
  - f: "tipo_veicolo_a"
    type: "Number"
    empty: 0.0
    uniq: 8
    doc: false
  - f: "tipo_veicolo_b"
    type: "Number"
    empty: 0.24
    uniq: 9
    doc: false
  - f: "tipo_veicolo_c"
    type: "Number"
    empty: 0.92
    uniq: 2
    doc: false
  - f: "eta_conducente_a"
    type: "Number"
    empty: 0.0
    uniq: 67
    doc: false
  - f: "eta_conducente_b"
    type: "Number"
    empty: 0.245
    uniq: 57
    doc: false
  - f: "eta_conducente_c"
    type: "Number"
    empty: 0.92
    uniq: 13
    doc: false
  - f: "n_pedoni_morti"
    type: "Number"
    empty: 0.0
    uniq: 1
    doc: false
  - f: "n_pedoni_feriti"
    type: "Number"
    empty: 0.0
    uniq: 3
    doc: false
  - f: "tot_morti_a_24ore_incidente"
    type: "Number"
    empty: 0.0
    uniq: 2
    doc: false
  - f: "tot_morti_a_30gg_incidente"
    type: "Number"
    empty: 0.0
    uniq: 1
    doc: false
  - f: "totale_feriti"
    type: "Number"
    empty: 0.0
    uniq: 6
    doc: false
  - f: "nome_strada"
    type: "Text"
    empty: 0.11
    uniq: 163
    doc: false
---
