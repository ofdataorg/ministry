---
title: "How We Score"
date: 2026-07-30
description: "Six axes, ten points each, one average — and the working published every time."
hidedate: true
toc: true
---

Every evaluation on this site scores a dataset on six axes, each out of ten, and reports the plain
unweighted mean. No secret weights, no composite index, no proprietary methodology. If you disagree
with a number, the reasoning is in the same page and you can argue with it.

## The six axes

### Completeness

Does the dataset cover what it claims to cover? We score coverage against the dataset's own stated
scope, not against an ideal. A national dataset is not penalised for stopping at the border. It is
penalised for gaps inside its own boundaries — missing regions, missing years, missing categories,
thresholds that silently exclude a long tail.

We also ask whether the gaps are *legible*. A dataset that documents where it is thin scores better
than one with identical holes and no coverage layer.

### Timeliness

The gap between when something happened and when you can read about it, plus whether the publisher
states a cadence and honours it. We are not scoring how recently the file changed — see
[Fresh Is a Claim, Not a Property](/analyses/fresh-is-a-claim-not-a-property/). A predictable annual
release with a documented six-month lag scores well. A live-looking page with no reference period
does not.

A dataset that has stopped being updated and says so scores better than one in the same condition
that says nothing.

### Documentation

Can a competent stranger use this correctly without asking anyone? We look for a data dictionary,
methodology, provenance, and — the part almost everyone skips — an honest account of limitations.
A publisher that tells you where its data is weak is doing the single most valuable thing
documentation can do.

Volume is not the metric. A clear ten-page guide beats four hundred pages of specification.

### Accessibility

How much friction stands between a person and the data. Registration walls, click-through
agreements, rate limits, captchas, portals that only export what fits on screen, download buttons
that email you a link tomorrow. Full marks means an open URL, a working API and no gate.

Cost is scored here too. We evaluate open datasets, but "free after registration" is not the same
as "free".

### Licensing

Can a reasonable person determine, without legal advice, what they are permitted to do? Full marks
for a single standard licence applied to the whole product with no user-class distinctions. Marks
off for bespoke terms, per-record patchworks, non-commercial restrictions, and — the worst case —
no stated terms at all.

We have written at length about why this axis punches above its weight in
[The Licence Is the Dataset](/analyses/the-licence-is-the-dataset/).

### Interoperability

How much work between download and analysis. Standard formats, stable identifiers, joinable
geography, machine-readable structure. Spreadsheets shaped for human reading — merged cells, stacked
headers, totals interleaved with detail — score badly here regardless of how good the underlying
statistics are.

Bespoke binary formats requiring community-maintained readers are the floor.

## Every score has a version and a date

An evaluation is not a verdict on a dataset. It is a verdict on **one version of that dataset,
examined on one day.** Publishers fix things. Series lapse. Licences get clarified. A score with no
stated basis is an opinion wearing a number, so every evaluation records two facts at the top:

- **Version** — what was assessed. A release number where the publisher issues one, a descriptor
  where they do not. Where a publisher does not version their data at all, the page says so, and
  that absence is itself a finding we score under interoperability.
- **Snapshot** — the date we pulled the data. Not the publication date of the review, and not the
  dataset's own last-updated field. The day we had the bytes.

Evaluations with a snapshot over a year old are flagged on the page as due for re-evaluation. We
would rather say "this is old" than let a stale score pass as current — it is the same failure we
score publishers down for in [Fresh Is a Claim, Not a Property](/analyses/fresh-is-a-claim-not-a-property/).

**Some evaluations carry no snapshot at all.** Those were written from the publisher's
documentation and prior working experience rather than from a dated download. They say so plainly
on the page. The scores stand as editorial judgement, but they are provisional until someone pulls
the data and verifies them, and they should not be quoted as measurement.

When a dataset is re-evaluated, the previous scoring stays on the page with its own version, date
and grade, so the movement is visible. Old grades are recomputed from their recorded axis scores by
the same code that computes the current one — a past grade is never hand-written either.

## Grades

The six scores are averaged and mapped to a letter. The letter is a summary, not the finding.

| Score | Grade | Reading |
|---|---|---|
| 9.2 – 10 | A+ | Reference quality. Copy this. |
| 8.5 – 9.1 | A | Excellent, with known limits. |
| 7.8 – 8.4 | A− | Strong. Minor friction. |
| 7.2 – 7.7 | B+ | Good, with one real weakness. |
| 6.5 – 7.1 | B | Solid and usable. Plan around the gaps. |
| 5.8 – 6.4 | B− | Useful, costly to work with. |
| 5.0 – 5.7 | C+ | Valuable substance, poor delivery. |
| 4.2 – 4.9 | C | Use only if nothing else exists. |
| 3.0 – 4.1 | D | Serious problems. Verify everything. |
| Below 3.0 | E | We would advise against it. |

## What we actually do

1. **Download it.** Not the sample, not the API demo. The real thing, at the size a real user takes.
2. **Open it cold.** We note how far we get on documentation alone before asking a human.
3. **Join it to something.** Almost every real use involves a join. Most problems surface there.
4. **Look for the seams.** Regional gaps, year breaks, category changes, geography revisions.
5. **Read the licence properly.** All of it, including the terms of use page nobody links to.
6. **Score, then write.** The prose has to justify the number. Where it cannot, the number changes.

## Our biases, stated

We evaluate from the position of someone who has to *use* the data — an analyst, a journalist, a
researcher with a deadline. That means we weight friction heavily and are unmoved by an institution's
reasons for it. A registration wall that exists for good internal reasons is still a wall.

We read English, and our evaluations of non-English-language datasets carry that limitation. Where
language affects the score, we say so explicitly in the review rather than burying it in the average.

We take no money from any publisher we evaluate, and we do not accept sponsored entries. If that
ever changes, it will be stated at the top of every affected page.

## Corrections

Scores are revisable and several already have been. If a publisher fixes something, tell us and we
will re-evaluate and date the change. If we got a fact wrong, tell us and we will correct it
visibly rather than quietly. Both routes go through [submissions](/submit/).
