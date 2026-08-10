# Ministry of Data

Hugo static site (extended, 0.128+) publishing evaluations and analyses of open datasets. Custom
theme in-repo — no external theme, no runtime third-party requests. Deploys to GitHub Pages via
Actions on push to `main`.

Grades are **computed** from the six-axis `scores` front matter in
`layouts/partials/func/score.html`, never written by hand. The reader-facing rubric is `/method/`.

## Design Context

### Users

Three audiences share every page, and the design has to serve all three without a mode switch:

- **Working data people** (analysts, data engineers, researchers) arriving mid-task. They want the
  verdict and the spec sheet in seconds, then the caveats. They scan; they do not read.
- **Journalists and researchers** sourcing data for a story or paper, usually unfamiliar with the
  dataset. They need the limitations loud and the licence unambiguous, because getting it wrong is
  published and permanent.
- **The broad open-data public**, arriving from a search or a shared link, mixed expertise, often on
  a phone. They need the front page to be striking and the language plain.

The practical consequence: **the scorecard must be readable at a glance and the prose must survive a
full read.** A design that only serves the skimmer fails the journalist; one that only serves the
reader fails the analyst.

### Brand Personality

**Official. Opinionated. Deadpan.**

A review desk with a grudge — open-data activism with a sense of humour. It names names, takes
sides, and enjoys the fight. Verdicts are blunt and unhedged, praise is specific and grudging, and
bad publishing practice is treated as a choice someone made rather than weather that happened.

The voice is unchanged, but it now speaks from behind a crest. The reference object is a
**Command Paper written by someone with a grudge**: the format of officialdom, the content of a
review desk that names names. Never neutral, never apologetic about having a view.

### Aesthetic Direction

**A government Command Paper.** Laid off-white stock, navy ink sampled from the crest
(`#051A38`), hairline and double rules, the arms at the top and numbered entries below.

The identity is the emblem: a globe on a classical column inside a laurel wreath whose branches
carry circuit traces and nodes, a compass star above, and MINISTRY OF DATA set beneath. It
replaced an earlier royal-arms lockup that read as too UK-specific — the institutional weight is
kept, the national claim is not.

It is a single-ink silhouette, which is why it is drawn as a CSS mask filled with the current
ink rather than shipped as artwork. The source file is near-black; the site renders it navy on
paper and off-white on navy, from one asset.

**Theme: light**, derived from the mark and from the register. Paper is warm (tinted toward 85°)
rather than neutral grey, so it reads as stock rather than as a screen.

**The joke is the gap.** The wrapper is straight-faced officialdom; the verdicts inside are
blunt, partisan and unhedged. Neither register winks at the other — the comedy only works if the
paper is played completely straight. Nothing should be styled to signal "this is a parody".

**Red is a rubber stamp.** The seal red appears only where something is being marked: a
correction, a failed axis, a warning, a link. It is never decoration.

**Anti-references:** the previous club-flyer treatment, enterprise SaaS dashboards, dark-mode
developer landing pages, and any ornament that cannot say what it encodes.

### Design Principles

1. **Play it straight.** The presentation is a government publication with no irony in the
   styling. All the attitude lives in the words. A design that also tries to be funny would
   flatten the joke and undercut the scoring.

2. **The emblem is the seal.** It marks authority — masthead, title page, footer. It is never
   stretched, distorted, or used as a texture. It is recoloured only by the ink token, which is
   how it survives the light/dark flip from a single file.

3. **Every ornament is a filing device.** Rules, entry numbers, section marks and score stacks
   all encode structure — position, score, boundary. If an element cannot say what it encodes,
   it comes out.

4. **The verdict is the interface.** The grade, the six axes and the one-line verdict are the
   primary objects on any evaluation. Prose supports them; it does not bury them.

5. **Partisan in words, precise in numbers.** The writing takes sides; the scoring does not. The
   two registers must stay visually distinct so the opinion never looks like the measurement.

### Type

- **Libre Caslon Display** — masthead, headings, figures. Caslon is the historic face of British
  state printing; the choice is the concept, not decoration.
- **Libre Caslon Text** — body. The same voice, cut for reading at length.
- **Public Sans** — UI, labels, tables, buttons. Literally a government typeface, and deadpan by
  design.
- **Spline Sans Mono** — figures, references, scores.

Anton, Barlow Condensed and Literata are gone with the club aesthetic. Inter, IBM Plex and the
rest of the default-grotesque set remain out — they are training-data reflexes and read as
generic.
