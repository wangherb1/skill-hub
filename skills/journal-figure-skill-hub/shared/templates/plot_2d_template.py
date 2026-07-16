from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from shared.scripts.export_plot import export_matplotlib

df = pd.read_csv(Path("source") / "raw_data.csv")
fig, ax = plt.subplots(figsize=(3.5, 2.4))
ax.plot(df["x"], df["y"], marker="o", label="Series")
ax.set_xlabel("Independent variable (unit)")
ax.set_ylabel("Response (unit)")
ax.legend(frameon=False)
export_matplotlib(fig, Path("final") / "figure", dpi=600)
