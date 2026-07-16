---
name: multi-panel-compositor
description: Combine panels into unified publication figures with consistent labels, spacing, and typography. Use whenever a figure contains multiple panels or combines plots, schematics, and images. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Multi-panel Compositor

## Applicability
Combine panels into unified publication figures with consistent labels, spacing, and typography.

## Inputs
- panel files
- composite_spec.json
- journal width
- caption draft

## Outputs
- composite SVG/PDF/PPTX/PNG
- panel mapping report
- caption draft

## Recommended Route
1. Use uniform labels such as (a), (b), (c).
2. Align axes and margins where possible.
3. Keep panel text readable at manuscript scale.
4. Avoid inconsistent color maps in comparable panels.

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
Use `multi-panel-compositor` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_multi_panel_compositor/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
