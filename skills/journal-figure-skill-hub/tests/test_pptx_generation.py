from pathlib import Path

def test_pptx_editable_copy_exists():
    root = Path(__file__).resolve().parents[1]
    pptx = root / "examples" / "demo_project" / "figures" / "Fig_04_generic_measurement_platform" / "editable" / "Fig_04_generic_measurement_platform.pptx"
    assert pptx.exists()
