---
name: data-plot-2d
description: Generate publication-quality 2D plots from structured data. Use for line, scatter, bar, box, violin, heatmap, contour, uncertainty, sensitivity, SHAP-style, and calibration plots. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# 2D Data Plot

## Applicability
Generate publication-quality 2D plots from structured data.

## Inputs
- figure_spec.json
- raw CSV/TSV/JSON data
- plot_config.json

## Outputs
- generate.py
- processed_data.csv
- PDF/SVG/PNG/TIFF exports
- QA report

## Recommended Route
1. Preserve raw data and create processed data explicitly.
2. Render with Matplotlib by default and optional SciencePlots styling.
3. Label axes and units, record scale transforms, and export vector plus 600 dpi preview.
4. Run preflight QA before delivery.

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
Use `data-plot-2d` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_data_plot_2d/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
