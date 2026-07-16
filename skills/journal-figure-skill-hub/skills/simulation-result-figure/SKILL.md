---
name: simulation-result-figure
description: Prepare FEA/CFD/multiphysics result figures without altering scientific field values. Use for stress, strain, temperature, velocity, pressure, contact, modal, fatigue, and phase-field maps. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Simulation Result Figure

## Applicability
Prepare FEA/CFD/multiphysics result figures without altering scientific field values.

## Inputs
- figure_spec.json
- original simulation exports
- software/version/export settings

## Outputs
- annotated composite
- color-scale log
- PDF/PNG/TIFF exports
- QA report

## Recommended Route
1. Keep original exports immutable under source/.
2. Record colorbar ranges, units, deformation scale, and software settings.
3. Use identical colorbar limits for comparable panels.

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
Use `simulation-result-figure` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_simulation_result_figure/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
