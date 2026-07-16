from pathlib import Path

def test_demo_plot_exports_exist():
    root = Path(__file__).resolve().parents[1]
    fig = root / "examples" / "demo_project" / "figures" / "Fig_01_model_performance_trend" / "final"
    assert (fig / "Fig_01_model_performance_trend.pdf").exists()
    assert (fig / "Fig_01_model_performance_trend.svg").exists()
    assert (fig / "Fig_01_model_performance_trend.png").exists()
