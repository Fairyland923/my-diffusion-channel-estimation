import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the file paths based on chronological order
files = [
    "results/dm_est/2026-03-11_16-18-50_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
    "results/dm_est/2026-03-12_22-16-51_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
    "results/dm_est/2026-03-14_18-25-15_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv",
    "results/dm_est/2026-03-14_18-41-28_3gpp_path=3_dim=64x16_valdata=10000_T=100_resamp=False_best_guided.csv"
]

labels = [
    "Prior only (from LS)",
    "MAP (from LS)",
    "MAP (from Gaussian)",
    "Prior only (from Gaussian)"
]

plt.figure(figsize=(10, 6))

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
linestyles = ['-', '--', '-.', ':']
markers = ['o', 's', '^', 'D']
linewidths = [3, 2, 2, 2]  # "Prior only (from LS)" 更粗

for i, (file, label) in enumerate(zip(files, labels)):
    if os.path.exists(file):
        df = pd.read_csv(file)
        plt.semilogy(
            df['SNR'], df['nmse_dm'],
            marker=markers[i],
            label=label,
            color=colors[i],
            linestyle=linestyles[i],
            linewidth=linewidths[i],
            markersize=8
        )
    else:
        print(f"File not found: {file}")

plt.title('NMSE vs SNR for Different Channel Estimation Methods')
plt.xlabel('SNR (dB)')
plt.ylabel('NMSE')
plt.grid(True, which="both", ls="--")
plt.legend()
plt.tight_layout()

output_path = "nmse_comparison.png"
plt.savefig(output_path)
print(f"Plot saved to {output_path}")
plt.show()
