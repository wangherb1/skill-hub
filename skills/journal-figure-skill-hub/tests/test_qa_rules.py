import json
from pathlib import Path

def test_qa_report_passes_for_demo_2d():
    root = Path(__file__).resolve().parents[1]
    report = root / "examples" / "demo_project" / "figures" / "Fig_01_model_performance_trend" / "qa" / "preflight_report.json"
    data = json.loads(report.read_text(encoding="utf-8"))
    assert data["status"] == "pass"
