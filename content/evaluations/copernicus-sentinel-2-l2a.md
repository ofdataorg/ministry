---
title: "Copernicus Sentinel-2 Level-2A"
date: 2026-06-30
publishers: ["European Space Agency", "European Commission"]
regions: ["Global", "Europe"]
place: "Global"
places: ["Global"]
domains: ["Earth Observation", "Climate", "Agriculture"]
licenses: ["Copernicus Open Licence"]

source: "https://dataspace.copernicus.eu/"
temporal: "2015 to present"
updated: "Daily"
cadence: "Twin-satellite constellation, roughly five-day revisit at the equator"
formats: ["JPEG2000 (SAFE)", "Cloud-Optimised GeoTIFF", "STAC"]
size: "Petabyte-scale archive"
access: "Free; registration for the Data Space Ecosystem, open mirrors on major clouds"
verdict: "Free, global, ten-metre, every five days, forever — the most generous public data programme ever run, if you can carry the weight."
reviewer: "Ministry desk"

scores:
  completeness: 9
  timeliness: 9
  documentation: 8
  accessibility: 7
  licensing: 10
  interoperability: 7

strengths:
  - "Full, free and open by policy, with no discrimination between research, commercial and public use."
  - "Systematic global acquisition — the archive is not driven by who paid for a tasking."
  - "Cloud-Optimised GeoTIFF and STAC catalogues on the public clouds mean you can query without downloading."
weaknesses:
  - "Level-2A atmospheric correction is good but not uniform; results over water, snow and haze need care and sometimes reprocessing."
  - "The SAFE directory structure is a hostile way to ship a raster and the community has spent a decade routing around it."
  - "Access moved from the Open Access Hub to the Data Space Ecosystem, and a lot of published code and tutorials still points at endpoints that no longer answer."

bestfor:
  - "Land cover, crop and vegetation monitoring at field scale"
  - "Change detection with a consistent multi-year baseline"
  - "Anything that needs global coverage without a procurement process"
avoidfor:
  - "Sub-ten-metre detail — that is a commercial-imagery question"
  - "Cloud-persistent tropics without an optical/radar fusion plan"
  - "Naive time series that ignore the cloud mask"
---

## What it is

Sentinel-2 carries a multispectral imager with thirteen bands at ten, twenty and sixty metres, and
it images the entire land surface systematically. Level-2A is the atmospherically corrected
bottom-of-atmosphere product: the one most users actually want, with a scene classification layer
and cloud probability shipped alongside.

The important thing about Copernicus is the policy, not the sensor. Full, free and open, for
everyone, permanently, with no distinction between a PhD student and a multinational. That decision
created an entire industry, and it remains the benchmark against which every other public data
programme should be judged.

## How it holds up

Coverage and cadence are outstanding. A five-day revisit from the twin-satellite constellation, a
decade-deep consistent archive, and a systematic acquisition plan mean you can ask questions across
time and space that simply were not askable before 2015.

Documentation is thorough and technically serious, though it is written for the remote-sensing
community rather than for a general data audience. The Product Definition and Algorithm Theoretical
Basis documents will answer any question you have, in about forty pages.

Accessibility is where marks come off, and the reasons are organisational rather than technical.
The migration to the Copernicus Data Space Ecosystem was the right architectural move, but it broke
a large body of published code and institutional pipelines that were pointed at the old hub. If you
inherit a Sentinel-2 workflow written before 2023, budget time to repoint it.

The SAFE format remains the archive's own worst enemy: a nested directory of JPEG2000 files and XML
metadata, per band, per tile. The community's answer has been the cloud mirrors, where the same data
sits as Cloud-Optimised GeoTIFF behind a STAC catalogue and behaves like something from this decade.
That workaround is now the mainstream path, which is a quiet indictment of the official one.

## Working with it

Query a STAC endpoint, filter on cloud cover and date, read only the bands and window you need.
Trust the scene classification layer for a first pass and verify it over water and bright surfaces,
where atmospheric correction is least reliable. For any multi-date composite, decide your cloud
masking strategy before you compute anything — it will move your result more than your choice of
index will.

## The call

Grade A−. On licensing it is a ten and deserves to be: this is what public data policy looks like
when it is done properly. The mark comes off for a delivery format that fights its users and a
platform migration that left a trail of broken pipelines. Neither of those is a reason to look
elsewhere. There is nowhere else with this coverage at this price, which is none.
