# roundtable-personas

Cover art for the [Roundtable](https://github.com/ai-automation-tools/roundtable) persona explorer, published as a static site by GitHub Pages.

```
https://ai-automation-tools.github.io/roundtable-personas/covers/<slug>.webp
```

`<slug>` is the persona's slug in Roundtable's `personas` table. Roundtable reads the base URL from `PERSONA_MEDIA_URL` and falls back to the persona's avatar when a cover is missing, so a persona without one is fine.

Avatars are not here: Roundtable stores those itself and serves them at `/avatars/<slug>`.

## Adding a cover

```bash
python add_cover.py <slug> path/to/cover.png   # writes covers/<slug>.webp
git add covers/<slug>.webp && git commit -m "Add cover: <slug>" && git push
```

Covers are 2:3 portraits, at most 720px wide, WebP quality 80. A push to `main` runs `.github/workflows/pages.yml`, which republishes the site in a minute or two.

## History

Started 2026-11-07 with the 101 covers from the AI-Automation-Library's retired Persona Registry (`My-Library/Content/Agent-Personas/`, now under `Archive/`). 20 of them are square, not 2:3: they were generated that way.
