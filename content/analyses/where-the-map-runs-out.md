---
title: "Where the Map Runs Out"
date: 2026-07-04
author: "Ministry desk"
description: "Global datasets are rarely global. They are dense where the observers are, and the gap is not random."
domains: ["Biodiversity", "Geospatial"]
regions: ["Global"]
toc: true
---

Every dataset in this catalogue that calls itself global is denser in some places than others, and
the pattern of that density is remarkably consistent. It follows money, institutions and observers.
It does not follow the phenomenon being measured.

This is not a complaint about any individual publisher. It is a property of how observation works,
and the only real failure is when a dataset does not tell you it is there.

## Three shapes of the same gap

**Volunteered data follows volunteers.** [OpenStreetMap](/evaluations/openstreetmap-planet/) is
extraordinary in Germany and skeletal in places with few mappers. The file gives you no field for
this. A road that does not exist in OSM and a road that nobody has mapped are byte-for-byte
identical, and a naive density comparison across two countries measures the mapping community, not
the road network.

**Scientific data follows research funding.** [GBIF](/evaluations/gbif-occurrence-records/) holds
billions of records, and they cluster in northern Europe and North America — regions with less
biodiversity than the tropics by a wide margin. Records concentrate near roads, near research
stations, and on weekends. Unweighted, GBIF produces beautiful maps of where biologists live.

**Statistical infrastructure follows state capacity.** Some countries publish
[individual-level mortality microdata back to 1979](/evaluations/datasus-sim-mortality/). Others
publish an annual PDF. That gap correlates with income, and it means cross-national health analysis
is systematically better informed about richer countries — including in the analyses that argue
about how resources should be distributed.

## Why "global" is the wrong word

A dataset with worldwide *extent* and uneven *density* gets described as global, and the word does
real damage. It signals to a reader that the comparison across places is valid, when the thing that
varies most across those places is often the observation process itself.

The honest description of most global datasets is: **worldwide in scope, with coverage that varies
by an order of magnitude and is not documented per region.** That sentence would prevent a great
deal of bad analysis, and almost no dataset says it.

## What publishers could do about it cheaply

We are not asking anyone to fix the underlying inequality of observation. Three much smaller things
would help:

- **Ship a coverage layer.** Per-country or per-cell record counts, effort proxies, last-updated
  dates. If you know your data is patchy, say where. This is usually one aggregation query away.
- **Distinguish zero from unknown.** A null and a measured zero are different facts. Datasets that
  collapse them force every downstream user to guess, and most guess wrong in the same direction.
- **Describe the collection process, not just the schema.** Who observed this, under what incentive,
  with what instrument? That paragraph is worth more than another ten columns.

## What analysts should do about it today

Assume unevenness until you have checked. Test your conclusion on a region you know well, then test
it on one you do not — if the finding is much stronger in the well-covered region, you may have
measured coverage. Correct for effort explicitly when the literature offers a method, and say so
when it does not.

And be careful with the specific claim that something is *absent*. Across this entire catalogue,
absence of a record almost never means absence of the thing. It usually means nobody was there to
write it down.
