from __future__ import annotations
import argparse, json
from datetime import datetime
from pathlib import Path

REQUIRED_DIRS = ["source", "code", "editable", "final", "qa", "caption"]

def qa(project: Path) -> dict:
    issues = []
    spec = project / "figure_spec.json"
    if not spec.exists():
        issues.append("Missing figure_spec.json")
        data = {}
    else:
        data = json.loads(spec.read_text(encoding="utf-8"))
    for d in REQUIRED_DIRS:
        if not (project / d).is_dir():
            issues.append(f"Missing directory: {d}")
    final_files = list((project / "final").glob("*")) if (project / "final").exists() else []
    editable_files = list((project / "editable").glob("*")) if (project / "editable").exists() else []
    if not final_files:
        issues.append("No final exports found")
    if not editable_files:
        issues.append("No editable outputs found")
    if data.get("ai_usage", {}).get("requires_disclosure") and not (project / "caption" / "ai_disclosure.md").exists():
        issues.append("AI disclosure required but missing")
    report = {
        "project": str(project),
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "figure_type": data.get("figure_type"),
        "final_files": [str(x.relative_to(project)) for x in final_files],
        "editable_files": [str(x.relative_to(project)) for x in editable_files],
        "issues": issues,
        "status": "pass" if not issues else "needs_fix",
    }
    qadir = project / "qa"
    qadir.mkdir(exist_ok=True)
    (qadir / "preflight_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    md = ["# Preflight QA Report", "", f"- Status: {report['status']}", f"- Figure type: {report.get('figure_type')}", ""]
    md.append("## Final files")
    md.extend(f"- {x}" for x in report["final_files"])
    md.append("\n## Editable files")
    md.extend(f"- {x}" for x in report["editable_files"])
    md.append("\n## Issues")
    md.extend(f"- {x}" for x in issues or ["None"])
    (qadir / "preflight_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (qadir / "issues_to_fix.md").write_text("\n".join(f"- {x}" for x in issues) + ("\n" if issues else "- None\n"), encoding="utf-8")
    return report

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("project")
    args = p.parse_args()
    print(json.dumps(qa(Path(args.project)), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
