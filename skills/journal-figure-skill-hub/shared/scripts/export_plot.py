from __future__ import annotations
from pathlib import Path

def export_matplotlib(fig, output_stem: str | Path, dpi: int = 600, tiff: bool = False) -> list[Path]:
    stem = Path(output_stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    outputs = []
    for ext in ["pdf", "svg", "png"]:
        path = stem.with_suffix(f".{ext}")
        fig.savefig(path, dpi=dpi if ext == "png" else None, bbox_inches="tight")
        outputs.append(path)
    if tiff:
        path = stem.with_suffix(".tiff")
        fig.savefig(path, dpi=dpi, bbox_inches="tight")
        outputs.append(path)
    return outputs
