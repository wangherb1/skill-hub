from __future__ import annotations
import argparse, shutil, subprocess
from pathlib import Path

def export_svg(svg: Path, out_dir: Path, dpi: int = 600) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    try:
        import cairosvg
        pdf = out_dir / f"{svg.stem}.pdf"
        png = out_dir / f"{svg.stem}_{dpi}dpi.png"
        cairosvg.svg2pdf(url=str(svg), write_to=str(pdf))
        cairosvg.svg2png(url=str(svg), write_to=str(png), dpi=dpi)
        outputs.extend([pdf, png])
    except Exception as exc:
        inkscape = shutil.which("inkscape")
        if not inkscape:
            raise RuntimeError(f"CairoSVG failed and Inkscape is unavailable: {exc}") from exc
        pdf = out_dir / f"{svg.stem}.pdf"
        png = out_dir / f"{svg.stem}_{dpi}dpi.png"
        subprocess.run([inkscape, str(svg), "--export-type=pdf", f"--export-filename={pdf}"], check=True)
        subprocess.run([inkscape, str(svg), "--export-type=png", f"--export-dpi={dpi}", f"--export-filename={png}"], check=True)
        outputs.extend([pdf, png])
    return outputs

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("svg")
    p.add_argument("--out-dir", default="final")
    p.add_argument("--dpi", type=int, default=600)
    args = p.parse_args()
    print("\n".join(str(x) for x in export_svg(Path(args.svg), Path(args.out_dir), args.dpi)))

if __name__ == "__main__":
    main()
