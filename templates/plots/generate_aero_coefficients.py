#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import math
import warnings
from pathlib import Path

import matplotlib
import numpy as np
from matplotlib.ticker import MultipleLocator

matplotlib.use("Agg")

warnings.filterwarnings(
    "ignore",
    message="Unable to import Axes3D.*",
    category=UserWarning,
)

import matplotlib.pyplot as plt


REFERENCE_AREA_M2 = math.pi * (0.127 ** 2) / 4.0
FORCE_FILE = Path("outputs_original/stream0/forces_bound1-wall.out")

MACH_CASES = {
    "M07": {"mach": 0.7, "dynamic_pressure_pa": 35.38e3},
    "M12": {"mach": 1.2, "dynamic_pressure_pa": 62.01e3},
    "M25": {"mach": 2.5, "dynamic_pressure_pa": 67.03e3},
}

AOA_CASES = {
    "A000": 0.0,
    "A025": 2.5,
    "A050": 5.0,
    "A075": 7.5,
    "A100": 10.0,
    "A125": 12.5,
    "A150": 15.0,
}

SHOW_LEGEND = True

PLOT_SERIES = {
    "present": {
        "label": "Present",
        "marker": "s",
        "markersize": 9,
        "markerfacecolor": "black",
        "markeredgecolor": "black",
        "markeredgewidth": 1.2,
    },
    "reference": {
        "CA": [
            {
                "enabled": True,
                "path": "ref_Miller_CA.csv",
                "label": "Miller",
                "marker": "o",
                "markersize": 9,
                "markerfacecolor": "white",
                "markeredgecolor": "black",
                "markeredgewidth": 1.2,
            },
        ],
        "CN": [
            {
                "enabled": True,
                "path": "ref_Miller_CN.csv",
                "label": "Miller (Exp.)",
                "marker": "o",
                "markersize": 9,
                "markerfacecolor": "white",
                "markeredgecolor": "black",
                "markeredgewidth": 1.2,
            },
            {
                "enabled": False,
                "path": "ref_Washington_CN.csv",
                "label": "Washington",
                "marker": "^",
                "markersize": 10,
                "markerfacecolor": "white",
                "markeredgecolor": "black",
                "markeredgewidth": 1.2,
            },
            {
                "enabled": True,
                "path": "ref_Dikbas_CN.csv",
                "label": "Dikbas (CFD)",
                "marker": "^",
                "markersize": 10,
                "markerfacecolor": "white",
                "markeredgecolor": "black",
                "markeredgewidth": 1.2,
            },
        ],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create CA/CN summary CSV files and plots for the M07, M12, and M25 "
            "CONVERGE cases."
        )
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Directory containing the M07, M12, M25 case folders.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "aero_summary",
        help="Directory where CSV files and plots will be written.",
    )
    parser.add_argument(
        "--tail-samples",
        type=int,
        default=500,
        help="Number of final samples to average from each force history.",
    )
    return parser.parse_args()


def load_mean_forces(force_path: Path, tail_samples: int) -> tuple[float, float]:
    data = np.loadtxt(force_path, comments="#", usecols=(0, 1, 3))
    if data.ndim == 1:
        data = data[np.newaxis, :]
    if data.size == 0:
        raise ValueError(f"No force data found in {force_path}")

    sample_count = min(tail_samples, len(data))
    tail_data = data[-sample_count:, 1:3]
    axial_force, normal_force = tail_data.mean(axis=0)
    return float(axial_force), float(normal_force)


def compute_coefficients(axial_force: float, normal_force: float, dynamic_pressure_pa: float) -> tuple[float, float]:
    scale = dynamic_pressure_pa * REFERENCE_AREA_M2
    return axial_force / scale, normal_force / scale


def write_csv(csv_path: Path, rows: list[dict[str, float]]) -> None:
    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["AOA", "CA", "CN"])
        for row in rows:
            writer.writerow(
                [
                    f"{row['AOA']:.1f}",
                    f"{row['CA']:.8f}",
                    f"{row['CN']:.8f}",
                ]
            )


def load_reference_points(reference_path: Path, mach_dir: str) -> tuple[np.ndarray, np.ndarray]:
    with reference_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError(f"Reference file has no header: {reference_path}")
        if "AOA" not in reader.fieldnames or mach_dir not in reader.fieldnames:
            raise ValueError(
                f"Reference file must contain 'AOA' and '{mach_dir}' columns: {reference_path}"
            )

        rows: list[tuple[float, float]] = []
        for row in reader:
            aoa_text = (row.get("AOA") or "").strip()
            coeff_text = (row.get(mach_dir) or "").strip()
            if not aoa_text or not coeff_text:
                continue
            rows.append((float(aoa_text), float(coeff_text)))

    if not rows:
        raise ValueError(f"No reference data found in {reference_path}")

    rows.sort(key=lambda item: item[0])
    aoa_values = np.array([item[0] for item in rows], dtype=float)
    coeff_values = np.array([item[1] for item in rows], dtype=float)
    return aoa_values, coeff_values


def reference_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 15,
            "axes.labelsize": 18,
            "axes.linewidth": 2.0,
            "xtick.labelsize": 14,
            "ytick.labelsize": 14,
            "xtick.major.width": 1.6,
            "ytick.major.width": 1.6,
            "xtick.major.size": 8,
            "ytick.major.size": 8,
        }
    )


def padded_limits(values: np.ndarray) -> tuple[float, float]:
    vmin = float(np.min(values))
    vmax = float(np.max(values))
    span = vmax - vmin
    magnitude = max(abs(vmin), abs(vmax), 1e-6)
    pad = max(0.12 * span, 0.03 * magnitude)

    lower = vmin - pad
    upper = vmax + pad

    if lower > 0.0:
        lower = max(0.0, lower)
    if upper < 0.0:
        upper = min(0.0, upper)

    return lower, upper


def snapped_limits(values: np.ndarray, step: float, start_at_zero: bool = False) -> tuple[float, float]:
    lower, upper = padded_limits(values)
    if start_at_zero:
        snapped_lower = 0.0
    else:
        snapped_lower = math.floor(lower / step) * step
    snapped_upper = math.ceil(upper / step) * step

    if math.isclose(snapped_lower, snapped_upper):
        snapped_upper = snapped_lower + step

    return snapped_lower, snapped_upper


def make_plot(
    plot_path: Path,
    series_list: list[dict[str, object]],
    ylabel: str,
    y_step: float | None = None,
    start_at_zero: bool = False,
    legend_loc: str = "best",
) -> None:
    reference_style()

    fig, ax = plt.subplots(figsize=(6.5, 5.0), dpi=200)
    all_y_values: list[np.ndarray] = []

    for series in series_list:
        aoa_values = np.asarray(series["aoa_values"], dtype=float)
        coeff_values = np.asarray(series["coeff_values"], dtype=float)
        all_y_values.append(coeff_values)
        ax.plot(
            aoa_values,
            coeff_values,
            linestyle="None",
            marker=series["marker"],
            markersize=series["markersize"],
            markerfacecolor=series["markerfacecolor"],
            markeredgecolor=series["markeredgecolor"],
            markeredgewidth=series["markeredgewidth"],
            label=series["label"],
        )

    present_aoa_values = np.asarray(series_list[0]["aoa_values"], dtype=float)
    limit_values = np.concatenate(all_y_values)

    ax.set_xlabel("AOA [deg]")
    ax.set_ylabel(ylabel)
    ax.set_xticks(present_aoa_values)
    ax.set_xlim(-0.3, 15.3)
    if y_step is None:
        ax.set_ylim(*padded_limits(limit_values))
    else:
        ax.set_ylim(*snapped_limits(limit_values, y_step, start_at_zero=start_at_zero))
        ax.yaxis.set_major_locator(MultipleLocator(y_step))
    ax.grid(True, which="major", linestyle=(0, (1.2, 2.4)), linewidth=0.8, color="0.35")
    ax.tick_params(direction="in", top=True, right=True, pad=8)
    if SHOW_LEGEND:
        ax.legend(
            frameon=True,
            facecolor="white",
            edgecolor="white",
            framealpha=1.0,
            loc=legend_loc,
        )

    fig.tight_layout()
    fig.savefig(plot_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def build_rows(base_dir: Path, mach_dir: str, dynamic_pressure_pa: float, tail_samples: int) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []

    for aoa_dir, aoa_deg in AOA_CASES.items():
        force_path = base_dir / mach_dir / aoa_dir / FORCE_FILE
        if not force_path.is_file():
            raise FileNotFoundError(f"Missing force file: {force_path}")

        axial_force, normal_force = load_mean_forces(force_path, tail_samples)
        ca, cn = compute_coefficients(axial_force, normal_force, dynamic_pressure_pa)
        rows.append({"AOA": aoa_deg, "CA": ca, "CN": cn})

    rows.sort(key=lambda row: row["AOA"])
    return rows


def build_plot_series(base_dir: Path, coefficient: str, mach_dir: str, rows: list[dict[str, float]]) -> list[dict[str, object]]:
    series_list: list[dict[str, object]] = [
        {
            "label": PLOT_SERIES["present"]["label"],
            "aoa_values": np.array([row["AOA"] for row in rows], dtype=float),
            "coeff_values": np.array([row[coefficient] for row in rows], dtype=float),
            "marker": PLOT_SERIES["present"]["marker"],
            "markersize": PLOT_SERIES["present"]["markersize"],
            "markerfacecolor": PLOT_SERIES["present"]["markerfacecolor"],
            "markeredgecolor": PLOT_SERIES["present"]["markeredgecolor"],
            "markeredgewidth": PLOT_SERIES["present"]["markeredgewidth"],
        }
    ]

    for reference in PLOT_SERIES["reference"][coefficient]:
        if not reference["enabled"]:
            continue
        reference_path = base_dir / reference["path"]
        aoa_values, coeff_values = load_reference_points(reference_path, mach_dir)
        series_list.append(
            {
                "label": reference["label"],
                "aoa_values": aoa_values,
                "coeff_values": coeff_values,
                "marker": reference["marker"],
                "markersize": reference["markersize"],
                "markerfacecolor": reference["markerfacecolor"],
                "markeredgecolor": reference["markeredgecolor"],
                "markeredgewidth": reference["markeredgewidth"],
            }
        )

    return series_list


def main() -> None:
    args = parse_args()
    base_dir = args.base_dir.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    for mach_dir, metadata in MACH_CASES.items():
        rows = build_rows(
            base_dir=base_dir,
            mach_dir=mach_dir,
            dynamic_pressure_pa=metadata["dynamic_pressure_pa"],
            tail_samples=args.tail_samples,
        )

        csv_path = output_dir / f"{mach_dir}_coefficients.csv"
        write_csv(csv_path, rows)

        ca_series = build_plot_series(base_dir, "CA", mach_dir, rows)
        cn_series = build_plot_series(base_dir, "CN", mach_dir, rows)

        make_plot(output_dir / f"{mach_dir}_CA.png", ca_series, r"$C_A$")
        make_plot(
            output_dir / f"{mach_dir}_CN.png",
            cn_series,
            r"$C_N$",
            y_step=0.05,
            start_at_zero=True,
            legend_loc="upper left",
        )

        print(f"Wrote {csv_path}")
        print(f"Wrote {output_dir / f'{mach_dir}_CA.png'}")
        print(f"Wrote {output_dir / f'{mach_dir}_CN.png'}")


if __name__ == "__main__":
    main()
