---
name: data-plot-3d
description: Generate 3D surfaces, contours, Pareto fronts, and high-dimensional scientific plots. Use for response surfaces, 3D scatter, contour-surface pairs, parameter maps, and field slices. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# 3D Data Plot

## Applicability
Generate 3D surfaces, contours, Pareto fronts, and high-dimensional scientific plots.

## Inputs
- figure_spec.json
- structured grid or point data
- viewpoint metadata

## Outputs
- static PDF/SVG/PNG exports
- viewpoint note
- QA report

## Recommended Route
1. Check whether a 2D contour communicates better than 3D.
2. Include colorbar units and viewpoint metadata.
3. Export a static journal version even if Plotly is used for exploration.
4. Avoid perspective choices that distort scientific interpretation.

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
Use `data-plot-3d` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_data_plot_3d/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
