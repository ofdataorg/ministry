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
| `scores` | Six axes, 0–10 each. The overall grade is computed, never hand-written |
| `verdict` | One quotable sentence; shows in the tracklist and on the scorecard seal |
| `strengths` / `weaknesses` | Rendered as the "Holds up" / "Falls down" panels |
| `bestfor` / `avoidfor` | Sidebar guidance lists |
| `source`, `temporal`, `updated`, `cadence`, `formats`, `size`, `access` | The spec sheet |

Scores are averaged with equal weight in `layouts/partials/func/score.html` and mapped to a letter
in `layouts/partials/func/grade.html`. Change the bands in one place and the whole site follows.

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

Late-nineties compilation-sleeve logic applied to dataset reviews: black stock, hazard stripes,
hand-set headlines, a numbered tracklist, scorecards drawn as EQ faders. The governing rule is
**loud shell, calm core** — full volume on the furniture, quiet and generously led in the article
body, because the reviews run 500+ words.

**Colour** is OKLCH throughout, so equal steps in lightness look equal. Neutrals are tinted toward
the brand hue (32°, red-orange) rather than the reflexive cool blue, which makes the greys and the
accent read as one material. `--hot` is for text on black; `--hot-deep` carries white text. Every
foreground/background pair in the palette clears WCAG AA.

**Chrome is a seal, not a style.** Metallic fill is restricted to three elements — the masthead
wordmark, the hero H1 and the scorecard grade seal. It is deliberately absent from body text, nav,
labels, buttons and the stat figures, which are solid ink. Spreading it further turns a mark of
authority into wallpaper.

**Type** pairs a heavy condensed display face with a serif body: Anton for headlines, Barlow
Condensed for UI and track titles, Literata for reading, Spline Sans Mono for data and numerals.
A serif body on a data site is against the reflex, and that is the point — it gives the
print-journalism register that partisan criticism needs.

**Tokens**: a 4pt spacing scale with semantic names (`--space-sm`, not `--spacing-8`), a five-step
type scale at roughly 1.28 ratio, fluid `clamp()` only where type is genuinely display-scale, and
exponential ease-out curves. Nothing animates a layout property. Components that need to respond to
their column rather than the viewport use `@container`.

Animation is suppressed under `prefers-reduced-motion`, and there is a print stylesheet.

## Content

Evaluations are editorial judgements about real, publicly available datasets. Scores are revisable —
see `/submit/` for corrections and re-review.

Text is CC BY 4.0. Fonts are under the SIL Open Font License.

## Deployment

Pushes to `main` build and publish via `.github/workflows/hugo.yml` (GitHub Actions → Pages).
`baseURL` is overridden at build time by `actions/configure-pages`, so the committed value in
`hugo.toml` only affects local builds — the live value follows whatever the Pages custom domain is
set to. The site is served from the custom domain `ministry.ofdata.org` at the site root.
