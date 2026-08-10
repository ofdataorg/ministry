---
title: "Regione Lombardia — Procedimenti a Istanza di Parte"
date: 2026-08-10
publishers: ["Regione Lombardia"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Governance"]
licenses: ["CC0 1.0"]

source: "https://www.dati.lombardia.it/d/mq6b-3uqx"
version: "Edition of 1 May 2021 — 702 procedures"
snapshot: 2026-08-10
temporal: "Position as at 1 May 2021"
updated: "1 May 2021"
cadence: "Declares Mai (never), with the convention explained on the page"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "702 procedures, 42 columns"
access: "Open API and bulk download, no registration"

verdict: "Seven hundred ways to apply to a regional government, each with a named official and a legal deadline — as they stood five years ago."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 5
  documentation: 3
  accessibility: 9
  licensing: 9
  interoperability: 6

strengths:
  - "**It explains its own `Mai` label** — the description states that a dataset published to a statutory deadline does not change except for corrections. The only publisher on this portal we have seen justify the convention."
  - "Real accountability content: each procedure carries its legal time limit in days, the responsible officer, the substitute-power holder, and the remedies available if the deadline passes."
  - "CC0, with the whole register downloadable in one request."
weaknesses:
  - "Zero of 42 columns documented, and the field names are doing the work instead — some run past seventy characters."
  - "Accented characters are stripped from field names, so `entità` becomes `entit` mid-word in several columns."
  - "Published to the position on 1 May 2021 and never superseded on the portal, so a reader today gets a five-year-old view of who is responsible for what."

bestfor:
  - "Administrative transparency research under Art. 35 D.Lgs 33/2013"
  - "Mapping statutory time limits across a regional government's services"
avoidfor:
  - "Contacting the official currently responsible for anything"
  - "Assuming the register reflects present organisational structure"
---

## What it is

Every procedure a member of the public can initiate with Regione Lombardia, published under Article
35 of Legislative Decree 33/2013 — Italy's administrative transparency law. 702 procedures, 42
columns: what the procedure is, who starts it, what to submit, the statutory deadline in days, the
officer responsible, the holder of substitute powers if that officer fails to act, and the legal
remedies available.

This is transparency data in the strict sense: not statistics about government, but the machinery of
government written down so a citizen can hold it to a timetable.

## How it holds up

**It does something no other dataset on this portal does: it explains its own metadata.** The
description states that `Frequenza di aggiornamento "Mai"` means the dataset, published at the
deadline the law sets, does not change except for errors and corrections.

That single sentence is worth flagging loudly. We spent an entire
[evaluation](/evaluations/dati-lombardia/) establishing that 444 datasets on this portal declare
themselves *Tempestiva* and sit seven years untouched — a vocabulary applied without meaning. Here
is a publisher using the same vocabulary, correctly, and taking the trouble to say what it means.
It is the difference between metadata and metadata theatre.

**The content is genuinely accountable.** `termine_di_conclusione_del_procedimento_in_gg` gives the
legal deadline in days. `nome_responsabile_procedimento` names the official. There are fields for the
substitute power holder and their telephone number, for the administrative and judicial remedies
available, and for whether self-declaration is accepted. Someone whose application has gone silent
past its deadline can find, in this file, who failed and what to do about it.

**The publishing craft is where it falls down.** Zero of 42 columns are documented. In fairness the
field names try to compensate, but they compensate to absurdity —
`telefono_responsabile_entit_organizzativa_competente_per_adozione_provvedimento` is a column name,
not a description, and at that length it is neither.

Note `entit` in the middle of it. Accented characters have been stripped rather than transliterated
when the field names were sanitised, so `entità` loses its final letter. It appears in several
columns. Harmless to a machine, and a small sign that nobody looked at the output.

**Timeliness is the real limit.** The register describes the position on 1 May 2021. Five years on,
officers have moved, organisational units have been restructured, and some deadlines have probably
changed. The `Mai` label is correct for *this edition* — but a transparency register is a living
obligation, and the portal offers this edition rather than a current one. The honest label
describes the file accurately while the underlying duty has moved on without it.

## Working with it

It is 702 rows; take the whole thing. Use `id_procedimento` as the key.

Treat every name and telephone number as historical. If you need to reach the responsible officer
today, use this to learn which organisational unit owns the procedure and then look that unit up
somewhere current.

## The call

**Grade B−.** The content is exactly what administrative transparency law was written to produce,
the licence is CC0, and — uniquely on this portal — the publisher explains its own update
convention instead of just asserting one. Those things are worth real credit.

What holds it back is age and absent documentation: a register of who is accountable, five years
stale, with 42 undocumented columns and a truncated accent in the field names. Republishing the
current edition would fix the biggest problem in a day.
