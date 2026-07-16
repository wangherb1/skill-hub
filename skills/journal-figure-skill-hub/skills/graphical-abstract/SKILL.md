---
name: graphical-abstract
description: Create graphical abstracts or TOC figures that summarize the central contribution. Use for journal graphical abstracts, TOC art, or one-screen conceptual summaries. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Graphical Abstract

## Applicability
Create graphical abstracts or TOC figures that summarize the central contribution.

## Inputs
- core contribution
- 3-5 visual modules
- journal requirements
- AI usage decision

## Outputs
- editable SVG/PPTX
- PDF/PNG exports
- ai_disclosure.md if needed

## Recommended Route
1. Summarize the paper's central contribution, not every detail.
2. Use no more than 3-5 visual modules.
3. For first-draft graphical abstracts, TOC figures, review-style overview figures, and advanced technical-roadmap figures, default to image generation using `shared/references/imagegen_prompt_bank.md`.
4. Keep generated text minimal and reserve label-safe spaces for later bilingual overlay.
5. Do not replace an image-generated first draft with a crude deterministic vector drawing merely because it is editable.
6. Use AI imagery only for non-evidentiary visual drafting unless disclosed and journal-compliant.

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
Use `graphical-abstract` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

## Example Output Directory
`figures/Fig_XX_graphical_abstract/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
