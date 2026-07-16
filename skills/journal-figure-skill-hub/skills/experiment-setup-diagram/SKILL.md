---
name: experiment-setup-diagram
description: Create diagrams of experimental platforms, measurement workflows, and data acquisition paths. Use for rigs, loops, battery aging systems, microscopy workflows, sensors, DAQ, and control systems. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Experiment Setup Diagram

## Applicability
Create diagrams of experimental platforms, measurement workflows, and data acquisition paths.

## Inputs
- figure_spec.json
- equipment modules
- sample location
- flow and signal definitions

## Outputs
- editable SVG/PPTX
- legend
- PDF/PNG exports
- QA report

## Recommended Route
1. For first-draft experimental setup or system diagrams, default to image generation using `shared/references/imagegen_prompt_bank.md` unless exact source CAD/photos must be preserved.
2. Show equipment modules, specimen position, sensor placement, DAQ/computer path, and physical/signal/control flow in the concept.
3. Separate material/energy flow, signal flow, and control flow by line style.
4. Always mark the sample/specimen position.
5. Add zoom-in panels when the measurement region is small.
6. Do not replace an image-generated first draft with a crude deterministic vector diagram merely because it is editable.
7. After concept selection, rebuild labels, arrows, legends, and critical geometry in editable SVG/PPTX.

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
Use `experiment-setup-diagram` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

For a high-quality concept draft, load `shared/references/imagegen_prompt_bank.md` and use the Experimental Setup Diagram Prompt.

## Example Output Directory
`figures/Fig_XX_experiment_setup_diagram/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
