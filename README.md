# skill-hub

Personal Codex skill repository for research writing, figure production, technical development, and agent workflows.

This repository is the GitHub source of truth for selected local Codex skills. Each installable skill lives under `skills/<skill-name>/` and exposes a `SKILL.md` file at that directory root.

## Skills

| Skill | Purpose | Local Codex path |
|---|---|---|
| `journal-figure-skill-hub` | Universal journal figure planning, generation, QA, and export workflow hub with sub-skills, shared schemas, examples, and validation scripts. | `C:\Users\wang_\.codex\skills\journal-figure-skill-hub` |
| `cn-human-writing-reviewer` | Conservative review and revision of Chinese-dominant academic, technical, patent, report, project, email, or bilingual text while preserving facts, terminology, structure, citations, and author voice. | `C:\Users\wang_\.codex\skills\cn-human-writing-reviewer` |
| `lean-execution` | Lightweight execution controller for bounded tasks where full process overhead would be disproportionate. | `C:\Users\wang_\.codex\skills\lean-execution` |

## Local Installation

From this repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install_to_codex.ps1
```

The installer copies each `skills/<name>` directory to `C:\Users\wang_\.codex\skills\<name>`.

After installation, restart or reload Codex so newly installed or updated skills are discovered.

## Validation

Run:

```powershell
python .\scripts\validate_skill_hub.py
```

The validator checks that every direct child of `skills/` contains `SKILL.md`, has YAML-style front matter, and declares a `name` matching its folder.
