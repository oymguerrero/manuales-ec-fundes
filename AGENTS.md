# Repository Guidelines

## Project Structure & Module Organization

This repository is a static Spanish-language learning site built with vanilla HTML, CSS, and JavaScript. `index.html` is the main landing page. `maestro/` contains the introductory manual; `estandar-a/` through `estandar-d/` contain each standard, with chapter pages such as `elemento-1.html`, preparation routes, resources, evaluation instruments, and downloadable `templates/`. Shared presentation and behavior live in `assets/styles.css` and `assets/interactive.js`. Keep images in `img/`, narration files and transcripts in `media/`, and asset-generation utilities in `scripts/`. Treat `design.md` as the canonical design-system reference. `extras/` is local-only and must not be committed.

## Build, Test, and Development Commands

There is no build step, framework, or package installation.

- Open `index.html` directly for a quick review.
- Run `python -m http.server 5500`, then visit `http://localhost:5500`, to test relative media paths reliably.
- Run `node --check assets/interactive.js` to validate JavaScript syntax.
- Run `python scripts/generate-templates.py` (or the `-b`, `-c`, or `-d` variant) only when regenerating standard templates.
- Load API credentials in PowerShell with `. .\scripts\load-env.ps1` before running TTS or image scripts.

## Coding Style & Naming Conventions

Use semantic HTML, shared CSS classes, and vanilla JavaScript; do not introduce frameworks or a build dependency. Follow the existing two-space indentation in HTML/CSS/JS and four spaces in Python. Use kebab-case for pages and assets (`ruta-preparacion.html`, `audio-estandar-b-e1-intro.mp3`) and `initX(container)` for interactive component initializers. Store component data beside its markup in `<script type="application/json">`. Preserve Mexican Spanish, UTF-8 accents, design tokens, WCAG AA contrast, and accessible SVG `<title>`/`<desc>` elements.

## Testing Guidelines

No automated test suite or coverage target exists. Before committing, check JavaScript syntax, parse any embedded JSON, and review changed pages at desktop and mobile widths. Exercise navigation, accordions, quizzes, audio, downloads, and browser-console errors. Confirm that content remains readable if JavaScript fails.

## Commit & Collaboration Guidelines

Recent commits use short imperative summaries, usually in Spanish, describing the exact change (for example, `Agregar recuadro gris...`). Keep commits focused and split diffs larger than roughly 500 lines. The team works directly on `main` without branches or pull requests: pull first, coordinate ownership of shared files, and use `git pull --rebase` if needed. Never commit `.env`, API keys, raw private source material, or files under `extras/`.
