# Ministry of Data

A review desk for open datasets: evaluations and analyses of public data from all over the world,
scored on six axes with the working published every time.

Built with [Hugo](https://gohugo.io/) (extended, 0.128+). No external theme — the layouts, CSS and
fonts all live in this repository, and the site makes no runtime requests to third parties.

Live at <https://odataorg.github.io/ministry/>.

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
static/fonts/   Anton, Barlow Condensed, Inter, IBM Plex Mono (latin subset, woff2)
```

## Design notes

Late-nineties club-flyer logic applied to dataset reviews: black canvas, chrome gradient wordmark,
hazard stripes, Anton display type, tracklists numbered like a compilation sleeve, and scorecards
rendered as EQ faders. Two accents — a hot orange-red and an acid yellow — over silver.

`--hot` is for text on black; `--hot-deep` carries white text at WCAG AA. Animation is
suppressed under `prefers-reduced-motion`, and there is a print stylesheet.

## Content

Evaluations are editorial judgements about real, publicly available datasets. Scores are revisable —
see `/submit/` for corrections and re-review.

Text is CC BY 4.0. Fonts are under the SIL Open Font License.

## Deployment

Pushes to `main` build and publish via `.github/workflows/hugo.yml` (GitHub Actions → Pages).
`baseURL` is overridden at build time by the Pages configuration step, so the committed value in
`hugo.toml` only affects local builds.
