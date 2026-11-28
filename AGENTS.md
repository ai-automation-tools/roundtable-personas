# AGENTS.md: roundtable-personas

Cover art for the [Roundtable](https://github.com/ai-automation-tools/roundtable) persona explorer, served by
GitHub Pages. Read by every agent CLI (Claude Code, Codex, Antigravity). [`README.md`](README.md) has the URL pattern and the steps.

- **Add covers only with `add_cover.py <slug> <image>`**: 2:3 portraits, at most 720px wide, WebP quality 80.
- **`<slug>` is the persona's slug in Roundtable's `personas` table.** A wrong slug is a cover nobody sees.
- **Avatars don't belong here**; Roundtable serves those itself.
- **This repo is public.** No personal data in images, names or commits.
- **Ship by PR to `main`**; `.github/workflows/pages.yml` republishes on merge.
