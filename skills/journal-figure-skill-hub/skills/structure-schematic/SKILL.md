---
name: structure-schematic
description: Create editable schematics of devices, assemblies, specimens, material layers, and geometric concepts. Use for physical structures, components, specimens, reactors, cells, modules, chips, sensors, and device layouts. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Structure Schematic

## Applicability
Create editable schematics of devices, assemblies, specimens, material layers, and geometric concepts.

## Inputs
- figure_spec.json
- reference sketch or geometry notes
- component list

## Outputs
- editable SVG
- editable PPTX
- PDF/PNG exports
- component legend

## Recommended Route
1. For first-draft structure schematics, default to image generation using `shared/references/imagegen_prompt_bank.md` unless a CAD/vector/reference source already provides a stronger visual basis.
2. Use image generation for visual ideation and polished structure concepts; do not treat generated geometry as evidence or as an exact CAD model.
3. Do not replace an image-generated first draft with a crude deterministic vector schematic merely because it is editable. Editable reconstruction is a later refinement step after the visual concept is accepted.
4. After the user selects a concept, rebuild final labels, arrows, callouts, and geometry as editable SVG/PPTX layers.
5. Keep shapes, labels, dimensions, arrows, and callouts as separate editable layers.
6. Use reference images only as trace/background sources.
7. Do not invent impossible geometry or unsupported dimensions.

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
Use `structure-schematic` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

For a high-quality concept draft, load `shared/references/imagegen_prompt_bank.md` and use the Structure Schematic Prompt.

For springs, seals, shafts, fixtures, boundary conditions, clamps, loading rigs, bearings, joints, contact interfaces, and related mechanical assemblies, use the Engineering Mechanical Schematic Prompt instead of the generic structure prompt.

## Example Output Directory
`figures/Fig_XX_structure_schematic/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
