from __future__ import annotations
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET

def has_text_layers(svg: Path) -> bool:
    root = ET.parse(svg).getroot()
    return any(el.tag.endswith("text") for el in root.iter())

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("svg")
    args = p.parse_args()
    ok = has_text_layers(Path(args.svg))
    print(f"text_layers={ok}")
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
