# Usage Guide

1. Create or receive a figure brief.
2. Run `shared/scripts/create_figure_project.py` to create a standard figure folder.
3. Fill or validate `figure_spec.json`.
4. Route to the relevant sub-skill under `skills/`.
5. Generate editable/vector outputs and final exports.
6. Run `shared/scripts/build_qa_report.py <figure-project>`.

Example:

```powershell
python shared\scripts\create_figure_project.py --figure-id Fig_06 --name battery_soh_trend --type data_plot_2d --out-root figures
python shared\scripts\validate_figure_spec.py figures\Fig_06_battery_soh_trend\figure_spec.json
```
