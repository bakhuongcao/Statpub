# Copilot instructions for this repo

Purpose: Short, actionable guidance to help AI coding agents be productive in this Quarto/R-based static site.

## Quick facts ✅
- Project type: Quarto website (see `_quarto.yml`). Source pages are `*.qmd` in the repo root.
- Output: generated site in `_site/` and various `*_files/` asset folders. _Do not edit generated files_ — change the source `.qmd`, CSS or JS instead.
- Code execution: Many `.qmd` pages execute R code (see `Descriptive statistics.qmd`, `Day_2.qmd`). Building the site runs these chunks by default (execute: eval: true).

## Build & preview (exact commands) 🔧
- Preview locally and auto-rebuild: `quarto preview` (run from repo root).
- Build static site: `quarto render` (or `quarto render --to html`).
- Use RStudio (project `stat.Rproj`) for interactive development if preferred.

## What to check before editing ✅ / quick checklist
- Avoid changing files in `_site/` — they are generated.
- Verify edits by running `quarto preview` and confirming the page renders without runtime errors.
- Ensure required R packages are available: pages use `pacman::p_load(...)` to load/install packages (see `Descriptive statistics.qmd`, `Day_2.qmd`). Be mindful that CI may not allow on-the-fly installs.
- Watch for absolute local data paths (example: `D:/.../data_file_Table_1.csv` in `Descriptive statistics.qmd` and `D:/PhD/.../epistat2024.sav` in `Day_2.qmd`). These are NOT portable — either parameterize these paths or ensure data is added to `resources/` or a `data/` folder and referenced relatively.

## Code / content patterns to follow
- R code chunks use knitr-style headers and Quarto execute options (example header in `Day_2.qmd` shows `execute: eval: true`, and chunk opts like `#| message: false`).
- Tables and Word exports are produced in R (e.g. `des_table1 |> as_flex_table() |> save_as_docx(...)`). Be aware builds may create side-effect files.
- Custom presentation assets live under `css/`, `custom_css/`, `components/`, and `js/`. Edits to these files reflect immediately in `quarto preview` output.

## Integration & external dependencies ⚠️
- External data: several pages reference external datasets using absolute paths (not checked into repo). Confirm data availability before running builds.
- No CI/test config found (no `.github/workflows` or unit tests). Treat building locally as the primary verification step.

## PR Guidance for agents
- Change source `.qmd`, `css/*`, or `components/*`. Run `quarto preview` and record a short verification note in the PR description (pages previewed, any package installs required, and any files generated).
- Do not commit `_site/` or generated `*_files/` unless the maintainer asked for a pre-built site; if you must, explicitly mention why.
- When fixing content that references local data paths, prefer adding a small note in the PR explaining how data can be provided (e.g., `resources/data/` with relative paths) or add a small guard that skips execution when files are missing.

## Language & localization
- The site contains Vietnamese and English text. When editing copy, preserve tone and language; do not translate content unless requested.

## Useful file references (examples)
- `Descriptive statistics.qmd` — demonstrates package-loading with `pacman` and a relative-to-absolute data path example.
- `Day_2.qmd` — R code examples for plotting and modeling; loads `.sav` files from an absolute path.
- `_quarto.yml` — site configuration, navigation, and layout references.
- `css/my_style.css`, `custom_css/style.css`, `components/*.js` — where to change styles and small interactive components.

---
If any of the above sections are unclear or you want me to add examples for a specific change (e.g., parameterizing data paths or adding a simple CI job for build verification), tell me which area and I'll iterate. ✨