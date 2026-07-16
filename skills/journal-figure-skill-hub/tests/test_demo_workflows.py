from pathlib import Path

def test_five_demo_projects_exist():
    root = Path(__file__).resolve().parents[1]
    figs = root / "examples" / "demo_project" / "figures"
    assert len([p for p in figs.iterdir() if p.is_dir()]) >= 5
