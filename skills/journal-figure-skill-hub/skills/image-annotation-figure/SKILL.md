---
name: image-annotation-figure
description: Annotate experimental photos, microscopy, segmentation, detection, and biomedical images. Use when real raster evidence needs scale bars, labels, overlays, or traceable annotations. Use inside journal-figure-skill-hub when planning, generating, editing, exporting, or checking publication-quality scientific figures.
---

# Image Annotation Figure

## Applicability
Annotate experimental photos, microscopy, segmentation, detection, and biomedical images.

## Inputs
- figure_spec.json
- immutable source image
- calibration data
- annotation plan

## Outputs
- annotated SVG/PDF/PNG
- preprocessing log
- QA report

## Recommended Route
1. Never fabricate or hallucinate visual evidence.
2. Keep annotations in vector layers.
3. Base scale bars on actual calibration.
4. Trace overlays to code and source data.
5. For style demonstrations only, AI image generation may create clearly marked synthetic observation/annotation concepts. Do not present these as real experimental evidence.
6. For real manuscript figures, use user-provided raw images and add editable annotation overlays.

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
Use `image-annotation-figure` to create a journal-ready figure from my data or figure brief. Create a `figure_spec.json`, preserve editable outputs, export PDF/SVG/PNG, and run preflight QA.

For a synthetic style demo only, load `shared/references/imagegen_prompt_bank.md` and use the Observation / Annotation Figure Prompt.

## Example Output Directory
`figures/Fig_XX_image_annotation_figure/`

## Handoff
- Route data-bearing panels to `data-plot-2d` or `data-plot-3d`.
- Route diagram panels to `structure-schematic`, `experiment-setup-diagram`, or `mechanism-diagram`.
- Route all multi-panel results to `multi-panel-compositor`.
- Finish every workflow with `figure-preflight-qa`.
