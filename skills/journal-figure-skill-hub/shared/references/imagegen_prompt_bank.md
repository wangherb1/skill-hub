# Image Generation Prompt Bank For SCI-Style Journal Figures

Use this bank when schematic quality matters more than deterministic editability in the first draft. Generate a high-quality raster concept first, then rebuild the accepted design as editable SVG/PPTX if needed.

## Non-Negotiable Rules

- Use AI image generation for visual drafting of structure schematics, experimental setup diagrams, mechanism diagrams, graphical abstracts, and complex observation/annotation concepts when simple vector drawing would look crude.
- Do not use AI image generation to invent experimental data, simulation fields, microscopy, medical images, failures, cracks, flames, morphologies, or measured evidence.
- If the image is evidence-like, mark it as synthetic concept art unless it is based on real user-provided data/images.
- Keep text minimal. Prefer numbered callouts or blank label areas because generated text can be unreliable; add final bilingual labels later in SVG/PPTX.
- Require a clean SCI review-article style: precise geometry, polished material rendering, restrained color, clear hierarchy, white/light background, no watermark, no logos, no decorative clutter.

## Shared Prompt Skeleton

```text
Use case: scientific-educational / infographic-diagram
Asset type: SCI journal figure concept draft, later rebuilt as editable PPT/SVG
Primary request: <figure type and scientific purpose>
Subject: <specific structure/system/mechanism>
Scientific content: <must show components, flows, states, causal chain, measurements>
Style/medium: high-end scientific illustration, clean 3D + vector hybrid, Nature/Advanced Materials review-article schematic quality
Composition/framing: <single wide panel or multi-panel layout>, clear reading order, generous margins
Typography: no unreliable text; use blank callout lines, small numbered circles, and label-safe whitespace
Color palette: restrained, colorblind-safe, white/light background, subtle shadows, no glossy marketing look
Constraints: scientifically plausible, no invented evidence, no watermark, no logo, no decorative icons, no messy text
Output intent: high-quality raster concept for review; editable reconstruction comes later
```

## Structure Schematic Prompt

```text
Create a high-quality SCI journal structure schematic concept for a generic engineered layered device/component.
Show an exploded 3D cutaway assembly with 4-6 physically plausible layers, seals/interfaces, fastening or constraint features, and a small zoom-in inset showing an interface cross-section.
Use polished technical illustration style suitable for a Nature/Advanced Materials review figure: clean white background, precise geometry, subtle depth, restrained blue/orange/gray palette, realistic but not photorealistic materials, clear hierarchy.
Add blank callout leaders and small numbered markers only; avoid readable text because final bilingual labels will be added later.
Composition: wide single-column figure, balanced left-to-right layout, enough blank margin for annotations.
Constraints: no impossible geometry, no brand/logo/watermark, no decorative clutter, no random text.
```

## Engineering Mechanical Schematic Prompt

Use this variant for springs, seals, shafts, fixtures, boundary conditions, clamps, loading rigs, bearings, joints, contact interfaces, and other mechanical-engineering structure schematics. This route is preferred over crude vector line art when the figure must visually communicate physical geometry and boundary-condition differences.

```text
Create a high-quality SCI journal engineering schematic concept for a mechanical component or boundary-condition comparison.
Show physically plausible 3D mechanical geometry with clear fixtures, plates, clamps, supports, loading arrows, reaction arrows, contact/interface regions, and deformation cues when relevant.
Use polished technical illustration style suitable for a mechanical engineering journal or Nature/Advanced Engineering Materials review figure: clean white or light-gray background, precise geometry, subtle depth, restrained blue/orange/teal/gray palette, realistic but not photorealistic metal and polymer materials, clear hierarchy.
For multi-panel comparisons, keep viewpoint, scale, component positions, lighting, and panel spacing consistent. Each panel should show one boundary condition or physical state, not a loose abstract icon.
Use only blank callout leaders, small numbered markers, arrows, and label-safe whitespace. Avoid readable generated text because final labels, formulas, and panel tags will be added later as editable layers.
Composition: wide journal figure, balanced left-to-right layout, enough margin for later annotations, no decorative clutter.
Constraints: mechanically plausible, no random text, no fake data, no logos, no watermark, no impossible geometry, no hand-drawn sketch, no black-only placeholder line art.
```

## Experimental Setup Diagram Prompt

```text
Create a high-quality SCI journal experimental setup schematic concept for a generic engineering measurement platform.
Show a realistic bench-scale system with specimen chamber, actuator/loading module, environmental or pressure/temperature control module, sensors near the specimen, DAQ unit, computer, and output data screen.
Represent physical flow with solid colored arrows and signal/control flow with dashed arrows; include a small magnified inset of the specimen-measurement region.
Style: clean 3D + vector hybrid scientific illustration, review-article quality, white background, precise equipment shapes, subtle shadows, restrained blue/orange/green palette.
Use small numbered markers and blank label areas only; final Chinese/English labels will be added later.
Constraints: scientifically plausible layout, no fake numerical readings, no logo, no watermark, no messy text.
```

## Mechanism Diagram Prompt

```text
Create a high-quality SCI journal mechanism schematic concept explaining a generic engineering failure/degradation mechanism.
Show a causal sequence from initial intact interface, external driving load/environment, micro-scale damage initiation, propagation/transport process, and observable macroscopic response.
Use 4 connected modules with arrows that clearly mean causality/transport/load transfer. Include one multi-scale inset showing macro device -> interface -> microstructure.
Style: polished Nature/Advanced Materials review-article mechanism figure, clean white background, semi-3D cutaway elements, crisp vector arrows, restrained colorblind-safe palette.
Use numbered markers and blank callout lines, not generated sentences; labels will be added later in editable bilingual layers.
Constraints: no invented experimental evidence, no decorative arrows, no random text, no watermark.
```

## Observation / Annotation Figure Prompt

```text
Create a high-quality synthetic demonstration figure for an experimental observation/annotation panel, clearly concept-style rather than real evidence.
Show a microscope-like grayscale observation region with a highlighted region of interest, clean contour overlay, scale-bar placeholder, zoom-in inset, and vector-style callouts.
Style: SCI journal result-panel design, clean annotation layers, precise overlays, no clutter, white margin for caption labels.
Use only minimal placeholder markings and no fake scientific numbers.
Constraints: mark as synthetic concept if text is used; no real-looking fabricated claim, no watermark, no logo.
```

## Graphical Abstract Prompt

```text
Create a high-quality SCI journal graphical abstract concept summarizing a general engineering research workflow.
Show 3-5 visual modules: problem/input, engineered system, mechanism/model, validation/output, and application impact.
Use a coherent left-to-right visual story, polished 3D + vector hybrid style, clean white background, minimal text-safe placeholders, subtle arrows, and restrained colorblind-safe palette.
Make it look like a professional TOC/graphical abstract for a high-impact engineering/materials journal.
Constraints: no fabricated data, no dense text, no logo, no watermark, no decorative clutter.
```
