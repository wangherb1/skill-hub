from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]

def validate(path: Path) -> list[str]:
    schema = json.loads((ROOT / "shared" / "schemas" / "figure_spec.schema.json").read_text(encoding="utf-8"))
    data = json.loads(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    return [f"{list(e.path)}: {e.message}" for e in validator.iter_errors(data)]

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("spec")
    args = p.parse_args()
    errors = validate(Path(args.spec))
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: {args.spec}")

if __name__ == "__main__":
    main()
