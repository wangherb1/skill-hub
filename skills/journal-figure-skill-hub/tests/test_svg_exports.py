from pathlib import Path
from shared.scripts.check_svg_text_layers import has_text_layers

def test_mechanism_svg_has_text():
    root = Path(__file__).resolve().parents[1]
    svg = root / "examples" / "demo_project" / "figures" / "Fig_03_general_mechanism_chain" / "editable" / "Fig_03_general_mechanism_chain.svg"
    assert has_text_layers(svg)
