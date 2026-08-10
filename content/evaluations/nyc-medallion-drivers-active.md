---
title: "NYC Active Medallion Drivers"
date: 2026-08-10
publishers: ["NYC Taxi and Limousine Commission"]
regions: ["North America"]
place: "New York City"
places: ["United States", "New York City"]
domains: ["Mobility", "Governance"]
licenses: ["None stated"]

source: "https://data.cityofnewyork.us/d/jb3k-j3gp"
version: "Rolling register — 179,962 active licences at snapshot"
snapshot: 2026-08-10
temporal: "Current register"
updated: "9 August 2026"
cadence: "Declares Daily, automated, and was current"
formats: ["CSV", "JSON", "RDF", "TSV"]
size: "179,962 rows, 6 columns"
access: "Open API and bulk download, no registration"

verdict: "A daily register of 180,000 licensed drivers by name, whose own description warns you to check whether it updated today."
reviewer: "Ministry desk"

scores:
  completeness: 6
  timeliness: 8
  documentation: 7
  accessibility: 9
  licensing: 3
  interoperability: 7

strengths:
  - "All 6 columns documented, and the register was genuinely current — updated the day before we pulled it, against a declared Daily cadence."
  - "**The description tells you how to check it.** It states the update window, tells the reader to verify the Last Update Date, and links to an alternative source if the file has gone stale."
  - "Small, clean and fast: 180,000 rows over the API in under a second, with no reshaping."
weaknesses:
  - "That same warning is an admission that the pipeline is not reliable, and the alternative source it points to is a Power BI dashboard rather than data."
  - "Six columns is thin for a licensing register — no vehicle, no base affiliation, no licence status beyond active membership of the file."
  - "It publishes 179,962 named individuals with licence numbers under no stated licence at all, which is an uncomfortable combination."

bestfor:
  - "Point-in-time counts of active medallion drivers"
  - "Licence expiry profiling across the workforce"
avoidfor:
  - "Historical analysis — the file is a snapshot and keeps no history"
  - "Assuming the file is current without checking `last_updated_date` first, as the publisher asks"
---

## What it is

Every active New York City medallion taxi driver in good standing: 179,962 rows, six columns —
licence number, name, licence type, expiry date, and the date and time the register was last
refreshed. The Taxi and Limousine Commission republishes it daily.

## How it holds up

**On its own terms it works.** All six columns are documented, the file was updated the day before we
pulled it against a declared Daily cadence, and 180,000 rows arrive in under a second. There is
nothing to clean.

**The description is the most interesting thing about it, and it cuts both ways.** It reads: the
dataset is updated daily between 4 and 7 PM; check the Last Update Date to confirm it shows today's
or yesterday's date; if it is older, find the latest data at a linked Power BI dashboard.

Read one way, that is exemplary. The publisher has told the reader precisely when to expect the
refresh, given them a field to verify it with, and provided a fallback. Compare it to the hundreds
of datasets across this catalogue that go quietly stale with no acknowledgement at all.

Read another way, it is an admission. A pipeline that needs a written warning telling users to check
whether it ran is a pipeline that does not always run. And the fallback is a dashboard, not data —
a human can look at it, a script cannot consume it. So the honest disclosure ends in a dead end for
the automated user, who is precisely the person most likely to be reading a daily register.

**Six columns is thin.** It says a person holds an active licence and when it expires. It does not
say what vehicle, which base, when the licence was first issued, or anything about status beyond
presence in the file. Because the file is a snapshot with no history, a driver who leaves simply
disappears — so attrition, entry rates and workforce turnover, which are the interesting questions
about a licensed workforce, are all unanswerable from this source unless you snapshot it yourself
daily.

**The licence question is sharper here than usual.** This is a register of nearly 180,000 named
individuals published with no stated terms of reuse. The names are public because taxi licensing is
a public register, and that is a legitimate transparency position. But "publicly available" and
"licensed for redistribution" are different things, and the portal's silence means anyone
republishing this — as several apps do — is doing so on an assumption.

## Working with it

Check `last_updated_date` before using it, exactly as the publisher asks. If you need a time series,
you must build it yourself by storing daily pulls; nothing here is retained.

Do not join on name. `license_number` is the key.

## The call

**Grade B.** Current, clean, fully documented and honest about its own reliability, which is more
than most daily feeds manage. It is held back by being a stateless six-column snapshot of a workforce
whose dynamics are the actual subject of interest, and by publishing 180,000 people's names with no
statement of what anyone may do with them.
