---
title: "Afrobarometer"
date: 2026-05-08
publishers: ["Afrobarometer"]
regions: ["Africa"]
place: "Pan-African"
places: ["Pan-African"]
domains: ["Governance", "Society"]
licenses: ["Free for non-commercial use, registration required"]

source: "https://www.afrobarometer.org/data/"
temporal: "1999 to present"
updated: "By survey round"
cadence: "Rounds roughly every two to three years"
formats: ["SPSS", "Stata", "CSV"]
size: "Nationally representative samples across around 40 African countries"
access: "Free download after registration"
verdict: "The most credible cross-national picture of African public opinion there is, and the methodology documentation to prove it."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 6
  documentation: 9
  accessibility: 7
  licensing: 6
  interoperability: 7

strengths:
  - "Full questionnaires, sampling protocols, fieldwork reports and weighting documentation published for every round."
  - "Genuinely comparative: a core question battery is held stable across countries and across rounds."
  - "Face-to-face, nationally representative probability samples in the respondent's own language — not an online panel wearing a national label."
weaknesses:
  - "Country coverage changes between rounds, so a balanced panel of countries is smaller than the headline count suggests."
  - "Round-to-round gaps of two to three years mean it cannot track fast-moving political events."
  - "Registration and non-commercial terms rule out a range of legitimate applied and commercial uses."

bestfor:
  - "Comparative attitudes to democracy, governance and service delivery"
  - "Trend analysis across African countries with consistent instruments"
  - "Survey design teaching — the documentation is a worked example"
avoidfor:
  - "Rapid response to current events"
  - "Sub-national estimates below the stratum the sample was designed for"
  - "Commercial products, without arranging terms first"
---

## What it is

A pan-African survey research network running nationally representative, face-to-face public
attitude surveys across roughly forty countries. Rounds cover democracy and governance, economic
conditions, service delivery, corruption, identity, and whatever the round's thematic modules add.
Interviews are conducted in respondents' own languages by national partner institutions.

## How it holds up

Documentation is where this scores highest, and deservedly. Every round publishes the full
questionnaire, the sampling protocol, the fieldwork report, the weighting scheme and the codebook.
You can reconstruct exactly what was asked, of whom, in what language, and how the weights were
built. In a field where "nationally representative" is frequently asserted and rarely evidenced,
Afrobarometer shows its working as a matter of course.

The comparative design is the second real strength. A stable core battery is carried across
countries and rounds, which is what makes cross-national and over-time comparison defensible rather
than aspirational. The methodological cost of maintaining that stability — resisting the urge to
improve question wording — is one most survey programmes fail to pay.

Completeness scores lower for a structural reason worth stating clearly: the set of countries
surveyed changes between rounds, driven by funding and by field conditions. The headline "around
forty countries" is a union across rounds, not a balanced panel. Anyone building a country-year
panel discovers this at the merge step, and the usable balanced set is meaningfully smaller.

Timeliness is inherent to the design. Face-to-face probability sampling across a continent takes
time and money; rounds land every two to three years. That is the right trade for measuring
underlying attitudes and the wrong instrument for tracking a coup, an election or a price shock.

Licensing costs it marks. Data is free but gated behind registration, and the terms are
non-commercial. For academic and civil society use that is workable. For an applied analyst inside a
company or a consultancy, it is a blocker that has to be resolved with the organisation directly.

## Working with it

Merge rounds on the documented core variables only, and check question wording between rounds before
trusting a trend — the codebook flags changes, and they matter. Apply the published weights; the
samples are stratified and unweighted results are not nationally representative. Respect the design
effect when computing standard errors. Do not push estimates below the geographic level the sample
was designed to support, however tempting the regional breakdown looks.

## The call

Grade B+. On documentation and comparative design this is exemplary work and the reference point for
survey research across the continent. Marks come off for an unbalanced country panel, an unavoidably
slow cadence, and licence terms that lock out a category of legitimate users.
