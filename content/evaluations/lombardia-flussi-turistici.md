---
title: "Lombardia — Monthly Tourist Flows by Province"
date: 2026-08-10
publishers: ["Regione Lombardia"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Economy", "Society"]
licenses: ["None stated"]

source: "https://www.dati.lombardia.it/d/xzck-giqt"
version: "2019–2024 series — 64,285 rows"
snapshot: 2026-08-10
temporal: "2019 to 2024"
updated: "4 August 2025"
cadence: "Declares Annuale; 371 days old, just inside the window"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "64,285 rows, 10 columns"
access: "Open API and bulk download, no registration"

verdict: "Arrivals and overnight stays by province, month and origin, split hotel from non-hotel — a properly built tourism series with no licence on it."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 6
  documentation: 8
  accessibility: 9
  licensing: 3
  interoperability: 8

strengths:
  - "**All 10 columns documented**, and the split that matters is present: arrivals and overnight stays, separately for hotel and non-hotel accommodation."
  - "Origin is resolved properly — Italian region for domestic visitors, country of origin for foreign ones — which is what makes market analysis possible."
  - "Tidy long format across province × month × origin, covering 2019 to 2024 so the pandemic collapse and recovery are both in the series."
weaknesses:
  - "**No licence stated**, on a portal where 82.1% of datasets are CC0. It is one of the 173 exceptions, and there is no obvious reason why."
  - "Declares an annual cadence and was 371 days old when measured — inside a generous window, but only just, and the series ends in 2024."
  - "`mese` is an Italian month name rather than a number, so chronological sorting requires a lookup."

bestfor:
  - "Tourism demand analysis for northern Italy by source market"
  - "Seasonality and pandemic recovery work at provincial level"
  - "Comparing hotel against extra-hotel accommodation shares"
avoidfor:
  - "Commercial products, until the licence question is answered"
  - "Sorting or joining on `mese` without mapping the month names first"
---

## What it is

Tourist arrivals and overnight stays in Lombardy's provinces, by month and by where the visitors came
from, split between hotel and non-hotel accommodation. 64,285 rows covering 2019 to 2024, with
Italian visitors resolved to their region of origin and foreign visitors to their country.

## How it holds up

**The structure is right and the documentation is complete.** All ten columns carry a description,
and the columns are the ones a tourism analyst would ask for: `arrivi` and `presenze` — arrivals and
overnight stays — reported separately for `alberghiero` and `extra_alberghiero`, plus totals.

That distinction is the substance of the dataset. Arrivals count visitors; presences count nights.
Their ratio is average length of stay, which is the single most useful derived measure in tourism
statistics and is computable directly here. Splitting hotel from non-hotel captures the shift toward
short-term rentals that has reshaped Italian tourism over exactly this period.

Resolving origin properly — region for domestic, country for foreign — rather than collapsing
everything to "Italian / foreign" is the other good decision. Source-market analysis is possible
because somebody kept the detail.

The window is well chosen by accident or design: 2019 to 2024 spans the pre-pandemic baseline, the
collapse, and the recovery, so the most interesting five years in modern Italian tourism are all in
one file.

**The licence is the anomaly.** This dataset states none. On a portal where **82.1% of holdings are
CC0** — a public domain dedication applied at scale, and the thing we praised most in the
[Lombardia evaluation](/evaluations/dati-lombardia/) — this is one of 173 exceptions. Nothing about
provincial tourism aggregates suggests a reason for special treatment. It looks like an omission
rather than a decision, which is the more frustrating explanation, because the regional default
would have covered it automatically.

The consequence is real. A consultancy building a market report on Lombard tourism has a clean CC0
answer for most of the portal and no answer for this file.

**Timeliness is adequate and drifting.** It declares `Annuale` and was 371 days old when we measured
it — inside a 400-day window, but not comfortably, and the series itself stops at 2024. An annual
tourism series published in August is already reporting on a season that ended eight months earlier;
that is normal for official statistics and worth knowing.

**One small friction:** `mese` holds Italian month names — *Agosto* — not numbers. Any sort or join
on time needs a name-to-number map, which is thirty seconds of work repeated by every user forever.

## Working with it

Map `mese` to an integer on load. Compute length of stay as `presenze_totale / arrivi_totale` and
sanity-check it — values far outside two to five nights usually indicate a small-cell artefact rather
than a finding.

Use the hotel/extra-hotel split rather than the totals where you can; the totals hide the structural
change.

Before publishing anything commercial, ask the region whether the portal's CC0 default was meant to
apply here.

## The call

**Grade B.** Well-structured, fully documented, tidy, and covering the right years — as a tourism
series it does everything asked of it. It is held back almost entirely by a missing licence on a
portal that gets licensing right 82% of the time, which makes this a clerical omission with real
consequences rather than a policy position.
