---
title: "Regione Lombardia — Procedimenti d'Ufficio"
date: 2026-08-10
publishers: ["Regione Lombardia"]
regions: ["Europe"]
place: "Lombardia"
places: ["European Union", "Italy", "Lombardia"]
domains: ["Governance"]
licenses: ["CC0 1.0"]

source: "https://www.dati.lombardia.it/d/3mbs-sdpm"
version: "Edition of 13 February 2014 — 138 procedures"
snapshot: 2026-08-10
temporal: "Position as at 13 February 2014"
updated: "20 February 2014"
cadence: "Declares Mai (never), with the convention explained"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "138 procedures, 35 columns"
access: "Open API and bulk download, no registration"

verdict: "The other half of a transparency obligation, published in 2014 and never since — accountability data older than the law is meant to keep it."
reviewer: "Ministry desk"

scores:
  completeness: 5
  timeliness: 2
  documentation: 2
  accessibility: 9
  licensing: 9
  interoperability: 5

strengths:
  - "Carries the accountable detail the law asks for: responsible officer, substitute-power holder, contacts, deadlines, and whether silenzio-assenso applies."
  - "Explains its own `Mai` label in the description, as its sibling does — this publisher understands the vocabulary it uses."
  - "CC0, and small enough to take whole in one request."
weaknesses:
  - "**Last updated 20 February 2014 — over twelve years before this review.** A register of who is currently responsible for what, frozen in 2014."
  - "Zero of 35 columns documented, and the field names are aggressively abbreviated: `cognome_uff_comp`, `tel_pot_sost`, `strumenti_corso_proc`, `uos`, `dgn`."
  - "138 procedures against 702 in the [companion dataset](/evaluations/lombardia-procedimenti-istanza-parte/), with no statement of why the two halves differ so much in size or currency."

bestfor:
  - "Historical research into Italian administrative transparency implementation"
  - "Comparing how the two halves of the Art. 35 obligation were published"
avoidfor:
  - "Anything about how Regione Lombardia is organised today"
  - "Contacting anybody named in it"
---

## What it is

The procedures Regione Lombardia initiates on its own motion — *d'ufficio*, as opposed to those
[started by a citizen](/evaluations/lombardia-procedimenti-istanza-parte/) — published under Article
35 of Legislative Decree 33/2013. 138 procedures, 35 columns: the title, the directorate, a
description, the responsible officer and their contacts, the holder of substitute powers, the legal
deadline, whether silence constitutes assent.

Together with its companion it is meant to be a complete public map of how the regional government
acts and who is answerable for it.

## How it holds up

**The intent is right and the two halves are wildly out of step.** The companion dataset covering
citizen-initiated procedures was published to the position on 1 May 2021 and carries 702 procedures.
This one was published to 13 February 2014 and carries 138.

Seven years apart, and a fivefold difference in count. Nothing on either page explains the gap.
A reader trying to assemble the complete Article 35 picture — which is the entire point of publishing
both — gets one half from 2021 and one from 2014, and has no way to know whether 138 is the true
number of own-motion procedures or simply what had been catalogued by 2014.

**On the cadence label we give the same credit we gave its sibling.** It declares `Mai` and the
description explains what that means: a dataset published at the deadline the law sets does not
change except for corrections. That is a publisher using its vocabulary honestly, which on
[this portal](/evaluations/dati-lombardia/) is rarer than it should be.

But the honesty of the label does not rescue the substance. `Mai` is correct for *this edition*. The
underlying obligation is continuous — Article 35 requires public bodies to keep this information
current — and what the portal offers is a twelve-year-old snapshot with no successor. The label
accurately describes a file that should have been superseded three governments ago.

**Documentation is zero of 35**, and here the field names cannot compensate the way they nearly did
in the companion dataset. That one had over-long but readable names. This one abbreviates hard:
`cognome_uff_comp`, `tel_pot_sost`, `email_pot_sost`, `strumenti_corso_proc`, `customer_satisf`,
`uos`, `dgn`. An Italian administrative specialist can decode most of them. Nobody else can, and
`dgn` — which holds values like `ORGANIZZAZIONE, PERSONALE` — is not guessable at all.

**The licence remains CC0**, which is the right answer and costs the region nothing.

## Working with it

Take it as a historical document about how Italy's transparency decree was implemented in its first
year, not as a current register. Read it beside the 2021 companion to see what changed in coverage
and structure between the two editions.

If you need the current position, the regional administrative portal rather than the open data
portal is where to look.

## The call

**Grade C+.** The content is exactly what the transparency decree intended, the licence is CC0, and
the publisher explains its update convention rather than asserting one — all real credit.

It is dragged down by being twelve years stale on an obligation that is ongoing, by 35 undocumented
and heavily abbreviated columns, and by sitting alongside a companion dataset seven years newer with
no explanation of the relationship. Republishing the current edition would cost a day and would fix
the largest problem on the page.
