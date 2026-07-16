from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image

def check(path: Path) -> dict:
    with Image.open(path) as img:
        dpi = img.info.get("dpi", (0, 0))
        return {"file": str(path), "width_px": img.width, "height_px": img.height, "dpi": dpi}

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("image")
    args = p.parse_args()
    print(check(Path(args.image)))

if __name__ == "__main__":
    main()
