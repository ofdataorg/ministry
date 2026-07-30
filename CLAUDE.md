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

**Loud. Opinionated. Cheaply-printed.**

A review desk with a grudge — open-data activism with a sense of humour. It names names, takes
sides, and enjoys the fight. Verdicts are blunt and unhedged, praise is specific and grudging, and
bad publishing practice is treated as a choice someone made rather than weather that happened.

The reference object is a **fanzine and a record sleeve**: photocopied flyer energy, hand-set
headlines, a tracklist on the back, printed on cheap stock. Never neutral, never institutional,
never apologetic about having a view.

### Aesthetic Direction

Late-nineties superclub / compilation-sleeve logic applied to dataset reviews. Black canvas, hazard
stripes, chrome wordmark, hard rules, evaluations as a numbered tracklist, scorecards as EQ faders.

**Theme: dark**, derived from context — a reference site consulted at a desk mid-task and browsed at
night, and every aesthetic reference (club, sleeve, flyer) is a black-substrate medium.

**Chrome is permitted but contained** to three places: masthead wordmark, hero H1, scorecard grade
seal. Never on body text, navigation, labels, buttons or stat figures. Everything else is solid ink.

**Anti-references:** government open-data portal, enterprise SaaS dashboard, generic dark-mode
developer landing page with a purple-to-blue gradient, and any layout presenting the datasets as an
identical grid of rounded cards.

### Design Principles

1. **Loud shell, calm core.** Full maximalism on hero, tracklist, scorecards, nav and section
   furniture. The article body is quiet, generously led and highly readable — 500+ word reviews have
   to survive a full read on a black background.

2. **Chrome is a seal, not a style.** Metallic fill marks the three places that carry authority.
   Spreading it further would make it decoration and cost it its meaning.

3. **Every ornament is a filing device.** Stripes, track numbers, hard rules and fader meters encode
   structure — position in a list, score, section boundary. If an element cannot say what it
   encodes, it comes out.

4. **The verdict is the interface.** The grade, the six axes and the one-line verdict are the
   primary objects on any evaluation. Prose supports them; it does not bury them.

5. **Partisan in words, precise in numbers.** The writing takes sides; the scoring does not. The two
   registers must stay visually distinct so the opinion never looks like the measurement.

### Type

- **Anton** — display. The flyer voice: hero, section bands, page titles.
- **Barlow Condensed** — UI, labels, nav, buttons, track titles.
- **Literata** — body. Sturdy low-contrast serif built for long screen reading; holds up on black
  and gives the print-journalism register partisan criticism needs.
- **Spline Sans Mono** — data, numerals, metadata, scorecard values.

Inter, IBM Plex Mono, Space Grotesk and the rest of the default-grotesque set are deliberately out;
they are training-data reflexes and read as generic.
