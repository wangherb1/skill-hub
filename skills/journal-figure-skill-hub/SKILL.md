---
name: journal-figure-skill-hub
description: Universal skill hub for planning, generating, composing, exporting, and checking publication-quality journal figures across disciplines. Use when the user asks for paper figures, scientific schematics, experimental diagrams, mechanism diagrams, data plots, simulation result figures, graphical abstracts, figure captions, or journal-ready figure exports.
---

# Journal Figure Skill Hub

## Core Contract
Use this hub for scientific and journal-paper figures across mechanical engineering, materials, energy, batteries, AI/ML, biomedical engineering, civil engineering, robotics, thermal/fluid science, reliability, experimental systems, and simulation-driven studies.

Every figure must start from or produce a non-empty `figure_spec.json`, preserve source traceability, keep editable/vector outputs whenever possible, and finish with preflight QA plus direct visual review.

## Routing Rules
1. Need a figure plan or figure list: use `skills/figure-brief-builder`.
2. Numerical 2D data: use `skills/data-plot-2d`.
3. 3D or high-dimensional data: use `skills/data-plot-3d`.
4. Physical object, assembly, specimen, or device: use `skills/structure-schematic`.
5. Experimental rig, measurement workflow, signal/control path: use `skills/experiment-setup-diagram`.
6. Causal, physical, degradation, reaction, transport, or model mechanism: use `skills/mechanism-diagram`.
7. FEA/CFD/multiphysics contour or field result: use `skills/simulation-result-figure`.
8. Real photos, microscopy, segmentation, detection, or biomedical images: use `skills/image-annotation-figure`.
9. Multiple panels: use `skills/multi-panel-compositor`.
10. Graphical abstract or TOC figure: use `skills/graphical-abstract`.
11. Journal packaging/export: use `skills/journal-export`.
12. Always finish with `skills/figure-preflight-qa`.

## Global Rules
- Do not fabricate experimental, simulation, microscopy, medical, or image evidence.
- Data-bearing figures must be reproducible from source data and code.
- AI image generation is the default first-draft route for non-evidentiary conceptual figures, including engineering mechanism diagrams, engineering structure schematics, experimental setup/system diagrams, workflow/process diagrams, review-style summary figures, graphical abstracts, and advanced technical-roadmap figures with small visual modules. The goal of the first draft is visual quality and communicative power, not editability.
- Data plots, numerical response curves/surfaces, simulation field/contour results, microscopy/photos, and experimental evidence figures must not be invented with image generation. They must be generated from traceable data, solver exports, or immutable source images.
- AI image generation is allowed only for ideation or disclosed non-evidentiary visual material.
- Preserve raw data and original images under `source/`.
- Keep line art, plots, schematics, labels, arrows, and callouts editable.
- Maintain bilingual readiness for every figure: store text labels in a replaceable label map so Chinese-to-English and English-to-Chinese figure variants can be regenerated quickly without redrawing.
- For Chinese review Word drafts, produce and use Chinese-label figures first. English-label figures are backup/submission variants and should be regenerated from the same label map, not redrawn manually.
- Use SimSun/宋体 for Chinese text. Use Times New Roman for English letters, numbers, symbols, units, and formulas. Keep all normal figure text no larger than Chinese Word size 5, treated here as 10.5 pt maximum unless the user explicitly approves a larger graphical-abstract title.
- Fit journal figures for Word insertion: single-column large figures must not exceed 15.5 cm width; two-column side-by-side figures must not exceed 7.5 cm width per single figure. Height may vary, but labels must remain readable at the target width.
- Export at least one editable/vector file and one review-friendly raster preview.
- Store figure projects as `figures/Fig_XX_short_name/` with `source/`, `code/`, `editable/`, `final/`, `qa/`, and `caption/`.
- A legacy raster copied into a hub folder is only a wrapped placeholder. It is not a successful hub-generated figure unless the visual design has been rebuilt or explicitly accepted as-is.
- `figure_spec.json` must define scientific purpose, 5-second reader takeaway, panel messages, generation route, source/evidence status, and output files. Empty title/objective-style shells are not acceptable.
- After preflight QA, the final PNG preview or a contact sheet must be opened and visually inspected. Reject and revise figures with text overlap, clipped labels, excessive blank space, unreadable symbols, crude placeholder geometry, wrong routing, or no visible improvement over the legacy draft.
- Image generation is not considered complete until the selected image is saved into the figure project under `source/` or `final/` and can be reopened with local visual inspection. If the image generation tool shows an inline result but exposes no filesystem artifact, record a blocker and keep the figure in concept-prompt-ready state instead of passing delivery.
- Do not replace an image-generation first draft with a crude deterministic vector drawing merely because it is editable. Editable SVG/PPTX reconstruction is a later refinement route after the image-generated concept direction is accepted, unless the figure is a data plot or evidence figure that requires deterministic generation from source data.

## Required Workflow
1. Create or read `figure_spec.json`.
2. Route to the narrowest sub-skill.
3. Generate source-controlled code/templates.
4. Export PDF/SVG/PNG and optional TIFF/PPTX.
5. Run preflight QA.
6. Open the final preview/contact sheet and perform visual QA.
7. Report limitations and missing evidence explicitly.
