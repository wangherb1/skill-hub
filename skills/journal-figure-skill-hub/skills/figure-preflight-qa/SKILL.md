---
name: figure-preflight-qa
description: Run the final quality gate for traceability, editability, journal compliance, and readability. Always run at the end of a figure task. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Figure Preflight QA

## Applicability
Run the final quality gate for traceability, editability, journal compliance, and readability.

## Inputs
- figure_spec.json
- source files
- editable outputs
- final exports
- caption draft

## Outputs
- qa/preflight_report.md
- qa/preflight_report.json
- qa/issues_to_fix.md

## Recommended Route
1. Check required files, formats, resolution, and vector/editable outputs.
2. Check labels, units, legends, colorbars, and caption-panel consistency.
3. Flag AI disclosure, third-party image, and source-traceability risks.
4. Open the final PNG preview or a contact sheet and visually inspect it before delivery. Structural file checks are not sufficient.
5. Reject figures with overlapped text, clipped labels, excessive whitespace, unreadable symbols, crude placeholder geometry, missing intended panels, or no visible improvement over a legacy draft.

## Editable Layer Requirements
- Keep text, arrows, shapes, annotations, legends, panel labels, and callouts editable whenever the output is line art or schematic.
- For raster evidence, keep the source image immutable and place annotations in a separate vector layer.
- Export at least one editable/vector artifact and one review-friendly raster preview.

## Quality Checks
- Validate or create `figure_spec.json` before generation.
- Confirm source traceability and document missing evidence.
- Check labels, units, colorbars, scale bars, font size, panel labels, and caption consistency.
- Run `shared/scripts/build_qa_report.py` before delivery.
- Add `qa/visual_review.md` when direct visual inspection is performed, recording whether the figure is manuscript-ready, first-draft usable, or requires redraw.

## Example Prompt
Use `figure-preflight-qa` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_figure_preflight_qa/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
