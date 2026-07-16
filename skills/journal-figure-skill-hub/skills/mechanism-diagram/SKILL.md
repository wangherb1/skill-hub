---
name: mechanism-diagram
description: Create causal diagrams that explain mechanisms, processes, degradation, transport, or model logic. Use for conceptual, physical, failure, reaction, transport, architecture, and causal pathway figures. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Mechanism Diagram

## Applicability
Create causal diagrams that explain mechanisms, processes, degradation, transport, or model logic.

## Inputs
- figure_spec.json
- initial condition
- driving factors
- process states
- observable consequence

## Outputs
- editable SVG/PPTX
- mechanism statement
- PDF/PNG exports
- QA report

## Recommended Route
1. For first-draft mechanism figures, default to image generation using `shared/references/imagegen_prompt_bank.md` unless the figure is a data/evidence panel that must be generated from source data.
2. Build the image-generation prompt around the chain: initial condition -> driver -> intermediate process -> variable transformation -> observable result.
3. Include multi-scale hierarchy when relevant: macro system -> interface/process zone -> micro mechanism.
4. Assign arrow semantics in the prompt and later overlay: force, heat, mass, signal, information, sequence, or causality.
5. Keep generated text minimal. Prefer blank callout areas, numbered markers, arrows, panel spaces, and label-safe margins because final Chinese/English labels may be rebuilt later.
6. Use equations only when they clarify the mechanism; in first-draft image generation, equations should usually be placed in editable overlay or left as reserved label areas.
7. Do not replace an image-generated first draft with a crude deterministic vector diagram merely because it is editable. Editable SVG/PPTX reconstruction is a later refinement step after the visual concept is accepted.
8. After concept selection, rebuild final bilingual labels, arrows, equations, and callouts in editable SVG/PPTX when editability or submission polish is required.

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
Use `mechanism-diagram` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

For a high-quality concept draft, load `shared/references/imagegen_prompt_bank.md` and use the Mechanism Diagram Prompt.

## Example Output Directory
`figures/Fig_XX_mechanism_diagram/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
