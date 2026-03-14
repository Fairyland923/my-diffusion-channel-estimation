import os
import pandas as pd
import matplotlib.pyplot as plt


# 按时间先后顺序对应的导频数：16, 10, 14, 12, 8, 6
EXPERIMENTS = [
    (
        "results/dm_est/2026-03-14_20-18-34_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
        16,
    ),
    (
        "results/dm_est/2026-03-14_20-35-51_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
        14,
    ),
    (
        "results/dm_est/2026-03-14_20-41-04_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
        12,
    ),
    (
        "results/dm_est/2026-03-14_20-30-27_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
        10,
    ),
    (
        "results/dm_est/2026-03-14_20-46-35_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
        8,
    ),
    (
        "results/dm_est/2026-03-14_20-51-11_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
        6,
    ),
]


def main() -> None:
    plt.figure(figsize=(10, 6))

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown"]
    linestyles = ["-", "--", "-.", ":", (0, (3, 1, 1, 1)), (0, (5, 2))]
    markers = ["o", "s", "^", "D", "v", "P"]

    plotted = 0
    for idx, (csv_path, pilots) in enumerate(EXPERIMENTS):
        if not os.path.exists(csv_path):
            print(f"File not found: {csv_path}")
            continue

        df = pd.read_csv(csv_path)
        if "SNR" not in df.columns or "nmse_dm" not in df.columns:
            print(f"Invalid format (need SNR and nmse_dm): {csv_path}")
            continue

        plt.semilogy(
            df["SNR"],
            df["nmse_dm"],
            label=f"pilots={pilots}",
            color=colors[idx % len(colors)],
            linestyle=linestyles[idx % len(linestyles)],
            marker=markers[idx % len(markers)],
            linewidth=2,
            markersize=7,
        )
        plotted += 1

    if plotted == 0:
        print("No valid data file found. Nothing to plot.")
        return

    plt.title("MAP Channel Estimation: NMSE vs SNR under Different Pilot Counts")
    plt.xlabel("SNR (dB)")
    plt.ylabel("NMSE")
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.legend(title="Setting", fontsize=10)
    plt.tight_layout()

    output_path = "nmse_comparison_pilots.png"
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved to {output_path}")
    plt.show()


if __name__ == "__main__":
    main()
