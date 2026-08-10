---
title: "OpenStreetMap Planet"
date: 2026-06-22
publishers: ["OpenStreetMap Foundation"]
regions: ["Global"]
places: ["Global"]
domains: ["Mobility", "Geospatial"]
licenses: ["ODbL 1.0"]

source: "https://planet.openstreetmap.org/"
temporal: "2004 to this minute"
updated: "Minutely diffs, weekly full planet"
cadence: "Continuous"
formats: ["PBF", "XML", "Shapefile extracts"]
size: "Tens of gigabytes as compressed PBF"
access: "Direct download, no registration; regional extracts widely mirrored"
verdict: "The only global map you can actually hold, and the only one whose licence will follow you home."
reviewer: "Ministry desk"

scores:
  completeness: 7
  timeliness: 10
  documentation: 6
  accessibility: 8
  licensing: 6
  interoperability: 7

strengths:
  - "Minutely replication. Nothing else at global scale is this fresh, and it is fresh for free."
  - "Coverage in dense mapping communities exceeds commercial products, including footpaths, entrances and turn restrictions no vendor bothers with."
  - "Every object carries its full edit history and author — provenance right down to the node."
weaknesses:
  - "Completeness varies by an order of magnitude between a European city and a rural district in a country with few mappers."
  - "The tagging schema is a folk taxonomy: conventions, not constraints. `highway=track` means different things in different countries."
  - "ODbL share-alike is a genuine commercial hazard. Produce a derived database and you owe the world your derivation."

bestfor:
  - "Routing, geocoding and network analysis anywhere on earth"
  - "Basemaps you control end to end"
  - "Mapping places official cartography has never prioritised"
avoidfor:
  - "Uniform global comparisons of feature density"
  - "Anything where a share-alike obligation is unacceptable"
  - "Assuming a missing feature does not exist on the ground"
---

## What it is

A single file containing every node, way and relation anyone has ever contributed to OpenStreetMap,
republished weekly, with minutely diffs in between. Roads, buildings, rivers, shops, bus routes,
park benches. It is the only global vector map that you can download, host and modify without asking
anyone.

The freshness is not a marketing claim. A mapper edits a junction in Lagos and the change is in the
replication stream within minutes. No commercial provider releases at that cadence, because no
commercial provider can afford to.

## How it holds up

Completeness is the axis that decides whether OSM works for you, and there is no single answer to
it. In Germany, the Netherlands or urban Japan, OSM is more detailed than most paid alternatives.
In parts of Central Africa and Central Asia, the road network is a skeleton traced from satellite
imagery with no names and no surface tags. Both facts live in the same file under the same schema,
and nothing in the data marks the difference. Comparative work across regions has to model
completeness explicitly or it will measure mapper density and call it infrastructure.

Documentation scores middling for a specific reason: the wiki is enormous, genuinely useful, and
not normative. Tags are conventions agreed by practice, and practice diverges regionally. A
pipeline written against European tagging habits will misread Brazilian or Indian data in ways that
are quiet rather than loud — no parse errors, just wrong answers.

Then there is ODbL. It is a real open licence and it protects the commons effectively, which is
exactly why it is a hazard for anyone who has not read it. Share-alike attaches to *derived
databases*, and the boundary between a produced work you may keep and a derived database you must
share is a question organisations have paid lawyers real money to answer. If your legal position
depends on that line, get advice before you build, not after.

## Working with it

Take a regional extract rather than the planet unless you truly need the planet. Import through
osm2pgsql or Osmium into PostGIS, or read PBF directly if your tooling supports it. Pin the
replication sequence number for anything you need to reproduce — "OSM as of Tuesday" is not a
citable state otherwise.

Do not evaluate coverage by eye in the one city you know well. It is the most reliable way to
overestimate the whole dataset.

## The call

Grade B+. On timeliness it is a straight ten and nothing comes close. It loses ground on uneven
completeness that the data does not self-describe, a schema held together by convention, and a
licence whose obligations are real and frequently discovered late. For routing, geocoding and
basemaps it is the default and rightly so.
