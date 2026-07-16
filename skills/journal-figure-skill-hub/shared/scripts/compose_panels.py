from __future__ import annotations
import argparse, html, json, math
from pathlib import Path
from xml.etree import ElementTree as ET

def compose(spec_path: Path, output: Path) -> Path:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    width = int(spec.get("width", 1200))
    height = int(spec.get("height", 800))
    margin = int(spec.get("margin", 45))
    panels = spec["panels"]
    cols = int(spec.get("cols", math.ceil(math.sqrt(len(panels)))))
    rows = math.ceil(len(panels) / cols)
    cell_w = (width - margin * (cols + 1)) / cols
    cell_h = (height - margin * (rows + 1)) / rows
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append('<rect width="100%" height="100%" fill="white"/>')
    for i, panel in enumerate(panels):
        row, col = divmod(i, cols)
        x = margin + col * (cell_w + margin)
        y = margin + row * (cell_h + margin)
        label = panel.get("label", f"({chr(97+i)})")
        title = html.escape(panel.get("title", ""))
        parts.append(f'<g id="panel_{i+1}">')
        parts.append(f'<text x="{x}" y="{y-12}" font-family="Arial" font-size="22" font-weight="bold">{label}</text>')
        parts.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="#f8f8f8" stroke="#444" stroke-width="1"/>')
        img = panel.get("file")
        if img:
            href = html.escape(img)
            parts.append(f'<image href="{href}" x="{x+10}" y="{y+20}" width="{cell_w-20}" height="{cell_h-45}" preserveAspectRatio="xMidYMid meet"/>')
        parts.append(f'<text x="{x+12}" y="{y+cell_h-12}" font-family="Arial" font-size="14">{title}</text>')
        parts.append("</g>")
    parts.append("</svg>")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(parts), encoding="utf-8")
    return output

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("spec")
    p.add_argument("output")
    args = p.parse_args()
    print(compose(Path(args.spec), Path(args.output)))

if __name__ == "__main__":
    main()
