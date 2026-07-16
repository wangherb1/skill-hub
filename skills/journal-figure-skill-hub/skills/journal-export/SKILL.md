---
name: journal-export
description: Export figures according to generic or target-journal file, size, DPI, and font constraints. Use before manuscript insertion, submission packaging, or journal-specific conversion. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Journal Export

## Applicability
Export figures according to generic or target-journal file, size, DPI, and font constraints.

## Inputs
- figure_spec.json
- editable source
- target journal or generic preset

## Outputs
- PDF/SVG/PNG/TIFF/EPS as available
- export_log.json
- journal package

## Recommended Route
1. Apply single-column or double-column width presets.
2. Check DPI, font size, vector availability, and file size.
3. Record missing optional tools such as Inkscape or ImageMagick.

## Editable Layer Requirements
- Keep text, arrows, shapes, annotations, legends, panel labels, and callouts editable whenever the output is line art or schematic.
- For raster evidence, keep the source image immutable and place annotations in a separate vector layer.
- Export at least one editable/vector artifact and one review-friendly raster preview.

## Quality Checks
- Validate or create `figure_spec.json` before generation.
- Confirm source traceability and document missing evidence.
- Check labels, units, colorbars, scale bars, font size, panel labels, and caption consistency.
- Run `shared/scripts/build_qa_report.py` before delivery.

## Example Prompt
Use `journal-export` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_journal_export/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
