---
title: "The Licence Is the Dataset"
date: 2026-07-25
author: "Ministry desk"
description: "Ten evaluations in, the pattern is hard to miss: the licence decides more about a dataset's real-world value than the data in it."
domains: ["Governance"]
regions: ["Global"]
toc: true
---

We started scoring licensing as one axis of six, weighted like the rest. That was a mistake, and the
catalogue has been telling us so for months. Licensing is not one of six equal properties of a
dataset. It is the gate that determines whether the other five ever get to matter.

## The pattern

Look at where the catalogue clusters. The datasets people build durable things on top of —
[Sentinel-2](/evaluations/copernicus-sentinel-2-l2a/), the
[American Community Survey](/evaluations/american-community-survey/),
[ABS DataPacks](/evaluations/abs-census-datapacks/) — all share one property, and it is not
technical excellence. It is that a reasonable person can determine, in under a minute and without a
lawyer, exactly what they are allowed to do.

Now look at the ones that frustrate people. [HDX](/evaluations/humanitarian-data-exchange/) is
excellent infrastructure hosting a licence patchwork. [GBIF](/evaluations/gbif-occurrence-records/)
has world-class reproducibility and a per-record licence mix that means a single download can carry
three different sets of obligations. [DATASUS](/evaluations/datasus-sim-mortality/) publishes
irreplaceable microdata under terms nobody has written down.

None of those are data quality problems. All of them reduce actual use.

## Four failure modes

**Unstated terms.** The data is downloadable, everyone uses it, and no document says what is
permitted. This feels open until an institutional lawyer is asked to sign off, at which point the
project stops. Silence is not permission, and treating it as such is a decision to carry
unquantified risk.

**Patchwork inheritance.** A collection where each item carries its contributor's licence. Download
a thousand records, inherit the strictest term among them, and discover it after you have built the
product. The catalogue's convenience is exactly what makes this dangerous — bulk access is one click,
bulk compliance is a spreadsheet.

**Non-commercial gating.** Free for research, closed for everything else. This sounds like a modest
restriction and functions as a hard boundary, because "commercial" is undefined at the edges. Is a
consultancy's pro bono report commercial? A university spin-out? A journalist at a for-profit
newspaper? Users who cannot answer confidently do the safe thing, which is not to use the data.

**Share-alike surprise.** [OpenStreetMap](/evaluations/openstreetmap-planet/) is the canonical case.
ODbL is a good licence doing what it was designed to do — protect a commons from enclosure. It is
also a licence whose obligations attach to *derived databases*, a boundary that is genuinely subtle,
and organisations discover which side of it they are on late and expensively.

## What good looks like

The two highest licensing scores in the catalogue went to the Copernicus programme and to the
ABS. Neither did anything clever. They did the same three things:

1. **One licence for the whole product.** Not per-record, not per-contributor, not per-tier.
2. **A standard licence, unmodified.** CC BY 4.0 or an equivalent everyone's legal department has
   already reviewed. Bespoke terms mean bespoke review, every time, by every user.
3. **No distinction between classes of user.** No research/commercial split, no registration wall,
   no click-through that has to be captured and stored.

That is the entire recipe. It costs nothing and it multiplies reuse.

## The consequence for our scoring

We are not reweighting the axes — a single composite that secretly weights one input is worse than
an honest average. But we have changed how we read the number. A dataset scoring nine on everything
and four on licensing is not an eight-point-something dataset. It is a good dataset you may not be
able to use, and the scorecard should be read in that order.

For publishers, the takeaway is blunter. If you have limited effort to spend improving your
dataset this year, do not spend it on another column. Spend it on a sentence stating, unambiguously,
what anyone is allowed to do with the ones you already have.
