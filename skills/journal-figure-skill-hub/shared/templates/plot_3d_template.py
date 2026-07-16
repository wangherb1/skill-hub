from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from shared.scripts.export_plot import export_matplotlib

df = pd.read_csv(Path("source") / "surface_data.csv")
fig = plt.figure(figsize=(4.5, 3.2))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_trisurf(df["x"], df["y"], df["z"], cmap="viridis", linewidth=0.2)
ax.set_xlabel("x (unit)")
ax.set_ylabel("y (unit)")
ax.set_zlabel("response (unit)")
fig.colorbar(surf, ax=ax, shrink=0.65, label="response (unit)")
export_matplotlib(fig, Path("final") / "figure", dpi=600)
