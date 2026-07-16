from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
INDEX_PATH = REPO_ROOT / "skill-index.json"


def read_frontmatter(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        raise ValueError(f"{skill_file} does not start with front matter")
    match = re.match(r"---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"{skill_file} has malformed front matter")

    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def main() -> int:
    if not SKILLS_ROOT.is_dir():
        raise SystemExit(f"Missing skills directory: {SKILLS_ROOT}")

    with INDEX_PATH.open("r", encoding="utf-8") as f:
        index = json.load(f)
    indexed_names = {item["name"] for item in index.get("skills", [])}

    skill_dirs = sorted(p for p in SKILLS_ROOT.iterdir() if p.is_dir())
    if not skill_dirs:
        raise SystemExit("No skills found")

    errors: list[str] = []
    found_names: set[str] = set()
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue

        try:
            frontmatter = read_frontmatter(skill_file)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{skill_dir.name}: {exc}")
            continue

        declared_name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        found_names.add(skill_dir.name)

        if declared_name != skill_dir.name:
            errors.append(
                f"{skill_dir.name}: front matter name is {declared_name!r}, expected {skill_dir.name!r}"
            )
        if not description:
            errors.append(f"{skill_dir.name}: missing description")

    missing_from_index = found_names - indexed_names
    stale_index = indexed_names - found_names
    for name in sorted(missing_from_index):
        errors.append(f"{name}: missing from skill-index.json")
    for name in sorted(stale_index):
        errors.append(f"{name}: indexed but not present in skills/")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {len(skill_dirs)} skills validated")
    for skill_dir in skill_dirs:
        print(f"- {skill_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
