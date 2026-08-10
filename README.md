# Ministry of Data

A review desk for open datasets: evaluations and analyses of public data from all over the world,
scored on six axes with the working published every time.

Built with [Hugo](https://gohugo.io/) (extended, 0.128+). No external theme — the layouts, CSS and
fonts all live in this repository, and the site makes no runtime requests to third parties.

Live at <https://ministry.ofdata.org/>.

## Running it locally

```bash
hugo server -D      # http://localhost:1313/
hugo --gc --minify  # production build into ./public
```

## Adding an evaluation

```bash
hugo new content evaluations/some-dataset.md
```

The archetype at `archetypes/evaluations.md` ships with the full front matter. The fields that
matter:

| Field | Purpose |
|---|---|
| `publishers`, `regions`, `domains`, `licenses` | Taxonomies — these drive the filters and index pages |
| `version` | What was evaluated — a release number, or a descriptor if the publisher does not version |
| `snapshot` | The date the data was actually pulled. Omit it rather than inventing one |
| `history` | Prior scorings, each with its own date, version and axis scores |
| `scores` | Six axes, 0–10 each. The overall grade is computed, never hand-written |
| `verdict` | One quotable sentence; shows in the tracklist and on the scorecard seal |
| `strengths` / `weaknesses` | Rendered as the "Holds up" / "Falls down" panels |
| `bestfor` / `avoidfor` | Sidebar guidance lists |
| `source`, `temporal`, `updated`, `cadence`, `formats`, `size`, `access` | The spec sheet |

Scores are averaged with equal weight in `layouts/partials/func/scoremap.html` and mapped to a
letter in `layouts/partials/func/grade.html`. Change the bands in one place and the whole site
follows — including historical grades, which are recomputed from their recorded axis scores rather
than stored.

**Version and snapshot are the point.** An evaluation judges one version of a dataset on one day,
so `layouts/partials/provenance.html` renders both at the top of every review. A snapshot over a
year old flags the page as due for re-evaluation. An evaluation with *no* snapshot says plainly
that it was written from documentation rather than a verified pull — omitting the field is the
honest option, never a date you did not earn. Aggregate pages carry a `basis` line saying how many
of their evaluations rest on dated measurement.

The scoring rubric itself is documented for readers at `/method/`.

## The Index

`/places/` ranks jurisdictions on the same six axes, in the manner of the Global Open Data Index.
Places nest — `data/places.yaml` defines the tree (id, title, level, parent) and every evaluation
carries two keys:

- `place` — the single jurisdiction whose data it is, used for "published here" counts
- `places` — that jurisdiction plus every ancestor, which is what the taxonomy indexes, so a term
  page automatically rolls up everything beneath it

To add a jurisdiction, add a node to `data/places.yaml` and use its `title` in an evaluation. The
`id` must equal the urlized `title` — it is the term page slug.

Ranking happens only within a level, never across one. A place with no datasets of its own is
flagged `derived`; a place resting on fewer than three is flagged `thin`.

## Records

`content/records/` holds machine-measured dataset pages — one per dataset, generated from an actual
download rather than written. They carry no `scores`, only a `measured` block and a rule-based
`condition`, and they are **deliberately kept out of every taxonomy** so they cannot leak into The
Index or the region and domain pages. `/method/` states the rules for readers.

The generator lives outside the repo: it merges a Socrata Discovery API pull with per-dataset
download profiles and emits front matter. To extend the set, profile more datasets and regenerate —
the front-matter shape is the contract, and `layouts/records/` renders whatever it is given.

## Adding an analysis

```bash
hugo new content analyses/some-argument.md
```

Analyses are ordinary pages. Set `toc: true` for a sidebar table of contents.

## Structure

```
archetypes/     front matter templates
assets/css/     main.css (the house style) + self-hosted @font-face rules
assets/js/      tracklist filtering and sorting, mobile nav
content/        evaluations/, analyses/, and standalone pages
layouts/        baseof, home, section, taxonomy and single templates + partials
static/fonts/   Anton, Barlow Condensed, Literata, Spline Sans Mono (latin subset, woff2)
```

## Design notes

Full design context — audience, brand personality, principles — lives in `.impeccable.md` and is
mirrored into `CLAUDE.md`. Read it before changing anything visual.

The register is a **government Command Paper**: warm off-white stock, navy ink sampled from the
crest (`#051A38`), hairline and double rules, the arms at the top and numbered entries below. The
joke is the gap between the wrapper and the contents — the presentation is straight-faced
officialdom, the verdicts are not. Nothing is styled to signal parody; the comedy only works if the
paper is played completely straight.

**Colour** is OKLCH throughout. Papers are tinted warm (85°) so they read as stock rather than as a
screen; ink and greys are tinted toward the crest's hue. The seal red is used like a rubber stamp —
corrections, failed axes, warnings, links — never as decoration. Every foreground/background pair
clears WCAG AA, the tightest being 4.87:1.

**Type** pairs Caslon with a government sans: Libre Caslon Display for headings and figures, Libre
Caslon Text for reading, Public Sans for UI and tables, Spline Sans Mono for scores. Caslon is the
historic face of British state printing and Public Sans is literally a government typeface — the
choices are the concept, not decoration.

**The emblem** is in `brand/`, with derivation commands in `brand/README.md`. It is a single-ink
silhouette, so the site draws it as a CSS `mask-image` filled with the current ink — one asset that
renders navy on paper and off-white on navy, and never needs a reversed copy.

**Tokens**: a 4pt spacing scale with semantic names, a six-step type scale, exponential ease-out
curves. Nothing animates a layout property. Components that need to respond to their column rather
than the viewport use `@container`. Animation is suppressed under `prefers-reduced-motion`, and the
print stylesheet leans into what the screen design already is.

## Content

Evaluations are editorial judgements about real, publicly available datasets. Scores are revisable —
see `/submit/` for corrections and re-review.

Text is CC BY 4.0. Fonts are under the SIL Open Font License.

## Deployment

Pushes to `main` build and publish via `.github/workflows/hugo.yml` (GitHub Actions → Pages).
`baseURL` is overridden at build time by `actions/configure-pages`, so the committed value in
`hugo.toml` only affects local builds — the live value follows whatever the Pages custom domain is
set to. The site is served from the custom domain `ministry.ofdata.org` at the site root.
