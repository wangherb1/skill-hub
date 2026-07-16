from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "examples" / "capability_gallery"


def font_name(preferred: str, fallback: str = "DejaVu Sans") -> str:
    names = {f.name for f in font_manager.fontManager.ttflist}
    return preferred if preferred in names else fallback


FONT_EN = font_name("Times New Roman")
FONT_ZH = font_name("SimSun", FONT_EN)
MAX_PT = 10.5

matplotlib.rcParams["font.family"] = FONT_EN
matplotlib.rcParams["font.size"] = 8
matplotlib.rcParams["axes.unicode_minus"] = False


def save(fig: plt.Figure, name: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    png = OUT / f"{name}.png"
    svg = OUT / f"{name}.svg"
    pdf = OUT / f"{name}.pdf"
    fig.savefig(png, dpi=300, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    fig.savefig(pdf, bbox_inches="tight")
    plt.close(fig)
    return png


def add_text(ax, x, y, text, zh=False, size=8, **kw):
    ax.text(x, y, text, fontname=FONT_ZH if zh else FONT_EN, fontsize=min(size, MAX_PT), **kw)


def setup_canvas(width_cm=15.5, height_cm=7.0):
    fig, ax = plt.subplots(figsize=(width_cm / 2.54, height_cm / 2.54))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    return fig, ax


def structure_schematic():
    fig, ax = setup_canvas()
    ax.add_patch(Rectangle((1.0, 2.1), 8.0, 1.6, facecolor="#EEF4FA", edgecolor="#333", lw=1.2))
    ax.add_patch(Rectangle((1.0, 3.7), 8.0, 0.45, facecolor="#D7E8F7", edgecolor="#0072B2", lw=1))
    ax.add_patch(Rectangle((1.0, 1.65), 8.0, 0.45, facecolor="#F9E0CC", edgecolor="#D55E00", lw=1))
    for x in [2.4, 5.0, 7.6]:
        ax.add_patch(Circle((x, 2.9), 0.35, facecolor="white", edgecolor="#333", lw=1))
    add_text(ax, 1.1, 4.45, "结构示意 / Structure schematic", zh=True, size=10, va="center")
    add_text(ax, 1.3, 3.9, "上层材料", zh=True, size=8, va="center")
    add_text(ax, 7.0, 3.9, "Layer A", size=8, va="center")
    add_text(ax, 1.3, 1.85, "功能层", zh=True, size=8, va="center")
    add_text(ax, 7.0, 1.85, "Functional layer", size=8, va="center")
    ax.annotate("", xy=(5.0, 3.25), xytext=(5.0, 5.0), arrowprops=dict(arrowstyle="->", lw=1))
    add_text(ax, 5.15, 5.0, "load / 载荷", zh=True, size=8, va="center")
    return save(fig, "01_structure_schematic")


def experiment_setup():
    fig, ax = setup_canvas()
    boxes = [(0.8, 3.0, "样品\nSample"), (3.0, 3.8, "传感器\nSensor"), (5.2, 3.8, "DAQ"), (7.4, 3.8, "计算机\nComputer")]
    for x, y, label in boxes:
        ax.add_patch(Rectangle((x, y - 0.45), 1.35, 0.9, facecolor="#F7F7F7", edgecolor="#333", lw=1))
        add_text(ax, x + 0.675, y, label, zh=True, ha="center", va="center", size=8)
    ax.add_patch(FancyArrowPatch((2.15, 3.0), (3.0, 3.8), arrowstyle="->", mutation_scale=10, lw=1.2, linestyle="--", color="#D55E00"))
    ax.add_patch(FancyArrowPatch((4.35, 3.8), (5.2, 3.8), arrowstyle="->", mutation_scale=10, lw=1.2))
    ax.add_patch(FancyArrowPatch((6.55, 3.8), (7.4, 3.8), arrowstyle="->", mutation_scale=10, lw=1.2))
    ax.add_patch(FancyArrowPatch((0.9, 1.5), (8.8, 1.5), arrowstyle="->", mutation_scale=10, lw=1.8, color="#0072B2"))
    add_text(ax, 3.8, 1.2, "物理流 / physical flow", zh=True, size=8)
    add_text(ax, 3.3, 4.75, "试验系统示意 / Experimental setup", zh=True, size=10)
    return save(fig, "02_experiment_setup")


def mechanism_diagram():
    fig, ax = setup_canvas()
    labels = [("初始状态\nInitial", 1.1), ("驱动因素\nDriver", 3.3), ("中间机制\nMechanism", 5.5), ("可观测结果\nObservable", 7.7)]
    for label, x in labels:
        ax.add_patch(Rectangle((x, 2.4), 1.5, 1.0, facecolor="#EEF4FA", edgecolor="#0072B2", lw=1))
        add_text(ax, x + 0.75, 2.9, label, zh=True, ha="center", va="center", size=8)
    for x in [2.6, 4.8, 7.0]:
        ax.add_patch(FancyArrowPatch((x, 2.9), (x + 0.6, 2.9), arrowstyle="->", mutation_scale=10, lw=1.2))
    add_text(ax, 1.2, 4.5, "机制机理图 / Mechanism diagram", zh=True, size=10)
    add_text(ax, 3.6, 1.5, "每个箭头必须代表因果、传热、传质、信号或时序", zh=True, size=8)
    return save(fig, "03_mechanism_diagram")


def line_scatter():
    fig, ax = plt.subplots(figsize=(7.5 / 2.54, 5.4 / 2.54))
    x = np.linspace(0, 10, 30)
    y = 0.4 + 0.45 * (1 - np.exp(-x / 3))
    err = 0.03 + 0.015 * np.sin(x) ** 2
    ax.plot(x, y, "o-", label="Model A", lw=1)
    ax.fill_between(x, y - err, y + err, alpha=0.18)
    ax.set_xlabel("Time (s)", fontname=FONT_EN, fontsize=8)
    ax.set_ylabel("Response (a.u.)", fontname=FONT_EN, fontsize=8)
    ax.tick_params(labelsize=7)
    ax.legend(frameon=False, fontsize=7)
    ax.grid(alpha=0.25)
    return save(fig, "04_2d_curve_scatter_uncertainty")


def bar_chart():
    fig, ax = plt.subplots(figsize=(7.5 / 2.54, 5.2 / 2.54))
    cats = ["A", "B", "C", "D"]
    x = np.arange(len(cats))
    ax.bar(x - 0.16, [0.55, 0.61, 0.72, 0.78], width=0.32, label="Baseline", color="#0072B2")
    ax.bar(x + 0.16, [0.62, 0.70, 0.80, 0.88], width=0.32, label="Proposed", color="#D55E00")
    ax.set_xticks(x, cats, fontname=FONT_EN, fontsize=8)
    ax.set_ylabel("Metric (a.u.)", fontname=FONT_EN, fontsize=8)
    ax.tick_params(labelsize=7)
    ax.legend(frameon=False, fontsize=7)
    return save(fig, "05_grouped_bar_chart")


def heatmap_contour():
    fig, ax = plt.subplots(figsize=(7.5 / 2.54, 5.6 / 2.54))
    x = np.linspace(-2, 2, 80)
    y = np.linspace(-2, 2, 80)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(xx * 1.3) * np.cos(yy) + 0.15 * xx
    im = ax.contourf(xx, yy, z, levels=18, cmap="viridis")
    ax.contour(xx, yy, z, levels=8, colors="white", linewidths=0.35)
    ax.set_xlabel("Parameter A", fontname=FONT_EN, fontsize=8)
    ax.set_ylabel("Parameter B", fontname=FONT_EN, fontsize=8)
    cb = fig.colorbar(im, ax=ax)
    cb.set_label("Response (a.u.)", fontname=FONT_EN, fontsize=8)
    cb.ax.tick_params(labelsize=7)
    ax.tick_params(labelsize=7)
    return save(fig, "06_heatmap_contour")


def response_surface():
    fig = plt.figure(figsize=(7.5 / 2.54, 5.7 / 2.54))
    ax = fig.add_subplot(111, projection="3d")
    x = np.linspace(-2, 2, 45)
    y = np.linspace(-2, 2, 45)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(xx) * np.cos(yy) + 0.1 * xx
    surf = ax.plot_surface(xx, yy, z, cmap="viridis", linewidth=0, antialiased=True)
    ax.set_xlabel("A", fontname=FONT_EN, fontsize=8)
    ax.set_ylabel("B", fontname=FONT_EN, fontsize=8)
    ax.set_zlabel("Response", fontname=FONT_EN, fontsize=8)
    ax.tick_params(labelsize=7)
    fig.colorbar(surf, ax=ax, shrink=0.55, label="Response")
    ax.view_init(elev=28, azim=-135)
    return save(fig, "07_3d_response_surface")


def simulation_contour():
    fig, ax = plt.subplots(figsize=(7.5 / 2.54, 5.2 / 2.54))
    x = np.linspace(-3, 3, 140)
    y = np.linspace(-1.6, 1.6, 90)
    xx, yy = np.meshgrid(x, y)
    z = np.exp(-((xx - 0.8) ** 2 + (yy * 1.8) ** 2)) + 0.55 * np.exp(-((xx + 1.1) ** 2 + (yy * 1.2) ** 2))
    im = ax.imshow(z, extent=[x.min(), x.max(), y.min(), y.max()], origin="lower", cmap="turbo", aspect="auto")
    ax.add_patch(Rectangle((-0.2, -0.45), 1.1, 0.9, fill=False, edgecolor="white", lw=1))
    ax.set_xlabel("x (mm)", fontname=FONT_EN, fontsize=8)
    ax.set_ylabel("y (mm)", fontname=FONT_EN, fontsize=8)
    cb = fig.colorbar(im, ax=ax)
    cb.set_label("Synthetic field (a.u.)", fontname=FONT_EN, fontsize=8)
    cb.ax.tick_params(labelsize=7)
    ax.tick_params(labelsize=7)
    return save(fig, "08_simulation_contour_synthetic")


def graphical_abstract():
    fig, ax = setup_canvas(width_cm=15.5, height_cm=5.4)
    modules = [("Input\n输入", 1.0, "#E8F1FA"), ("Model\n模型", 3.6, "#FCE8D8"), ("Mechanism\n机理", 6.2, "#E9F6EF"), ("Output\n输出", 8.2, "#EFEFEF")]
    for text, x, color in modules:
        ax.add_patch(Rectangle((x, 2.25), 1.45, 0.9, facecolor=color, edgecolor="#333", lw=1))
        add_text(ax, x + 0.725, 2.7, text, zh=True, ha="center", va="center", size=8)
    for x in [2.45, 5.05, 7.65]:
        ax.add_patch(FancyArrowPatch((x, 2.7), (x + 0.85, 2.7), arrowstyle="->", mutation_scale=10, lw=1.2))
    add_text(ax, 1.0, 4.2, "Graphical abstract / 图文摘要", zh=True, size=10)
    add_text(ax, 1.0, 1.35, "3-5 个视觉模块，概括核心贡献，不替代真实证据", zh=True, size=8)
    return save(fig, "09_graphical_abstract")


def image_annotation():
    fig, ax = plt.subplots(figsize=(7.5 / 2.54, 5.0 / 2.54))
    rng = np.random.default_rng(7)
    base = rng.normal(0.45, 0.08, (90, 140))
    yy, xx = np.ogrid[:90, :140]
    mask = ((xx - 78) ** 2 / 30 ** 2 + (yy - 47) ** 2 / 19 ** 2) < 1
    img = base.copy()
    img[mask] += 0.25
    ax.imshow(img, cmap="gray", vmin=0, vmax=1)
    ax.contour(mask, levels=[0.5], colors=["#D55E00"], linewidths=1)
    ax.plot([15, 55], [80, 80], color="white", lw=2)
    add_text(ax, 15, 75, "20 μm", size=7, color="white")
    ax.axis("off")
    add_text(ax, 6, 10, "合成示例 / synthetic annotation", zh=True, size=8, color="white")
    return save(fig, "10_image_annotation_synthetic")


def contact_sheet(paths: list[Path]) -> Path:
    labels = [
        "Structure schematic",
        "Experimental setup",
        "Mechanism diagram",
        "2D curve/scatter",
        "Grouped bar",
        "Heatmap/contour",
        "3D response surface",
        "Simulation contour",
        "Graphical abstract",
        "Image annotation",
    ]
    fig, axes = plt.subplots(5, 2, figsize=(15.5 / 2.54, 20 / 2.54))
    for ax, path, label in zip(axes.ravel(), paths, labels):
        img = plt.imread(path)
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(label, fontname=FONT_EN, fontsize=8)
    fig.tight_layout(pad=0.8)
    return save(fig, "00_capability_gallery_contact_sheet")


def main() -> None:
    paths = [
        structure_schematic(),
        experiment_setup(),
        mechanism_diagram(),
        line_scatter(),
        bar_chart(),
        heatmap_contour(),
        response_surface(),
        simulation_contour(),
        graphical_abstract(),
        image_annotation(),
    ]
    label_map = {
        "policy": {
            "zh_font": "SimSun/宋体",
            "en_font": "Times New Roman",
            "max_font_pt": 10.5,
            "single_large_width_cm": 15.5,
            "two_panel_each_width_cm": 7.5,
        },
        "available_examples": [p.name for p in paths],
    }
    (OUT / "label_map.json").write_text(json.dumps(label_map, ensure_ascii=False, indent=2), encoding="utf-8")
    contact = contact_sheet(paths)
    print(contact)


if __name__ == "__main__":
    main()
