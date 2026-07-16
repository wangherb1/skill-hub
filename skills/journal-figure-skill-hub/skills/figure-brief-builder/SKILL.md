---
name: figure-brief-builder
description: Convert a paper outline, abstract, or draft into a minimal evidence-driven figure plan. Use first when the user needs a figure list, figure map, caption skeleton, or generation plan. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Figure Brief Builder

## Applicability
Convert a paper outline, abstract, or draft into a minimal evidence-driven figure plan.

## Inputs
- paper title
- abstract or section outline
- target journal
- available data or visual evidence

## Outputs
- figure_list.md
- figure_map.json
- figure_spec.json drafts
- caption skeletons

## Recommended Route
1. Identify central claims and evidence gaps.
2. Map each claim to the minimum necessary figure.
3. Classify figure type and panel structure.
4. Assign a reproducible generation route.
5. Flag missing data, missing images, and unresolved journal constraints.

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
Use `figure-brief-builder` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_figure_brief_builder/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
