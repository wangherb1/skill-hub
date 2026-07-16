# Journal Figure Skill Hub

This is a reusable, discipline-neutral Codex skill hub for planning, generating, editing, composing, exporting, and quality-checking publication-ready journal figures.

The hub is not tied to one thesis topic. It supports data plots, schematics, experimental diagrams, mechanism diagrams, simulation figures, image annotations, multi-panel composites, graphical abstracts, export packaging, and preflight QA.

## Quick Start

```powershell
cd E:\Codex\Paper_work\journal-figure-skill-hub
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe shared\scripts\make_demo_figures.py
.\.venv\Scripts\python.exe -m pytest
```

Every real figure should start from `figure_spec.json` and end with `qa/preflight_report.md`.

For complex schematics, mechanism diagrams, experimental setup diagrams, and graphical abstracts, the first draft should use the SCI-style image generation prompts in `shared/references/imagegen_prompt_bank.md`. After the user selects a concept, rebuild labels, arrows, and required geometry in editable SVG/PPTX.

## Codex Skill Use

Use the root `SKILL.md` as the router. For global discovery, copy or symlink this folder into `C:\Users\wang_\.codex\skills\journal-figure-skill-hub` after reviewing the local implementation.
