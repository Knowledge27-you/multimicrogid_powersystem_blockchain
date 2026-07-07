import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# Create Output Folder
# ==========================================================

os.makedirs("heatmaps", exist_ok=True)

sns.set_theme(style="white")

# ==========================================================
# 1. Trading Matrix Heatmap
# ==========================================================

trades = pd.read_csv("simulation_results.csv")

trade_matrix = trades.pivot_table(
    index="Prosumer",
    columns="Consumer",
    values="Energy Traded",
    aggfunc="sum",
    fill_value=0,
    observed=False
)

plt.figure(figsize=(10,8))

sns.heatmap(
    trade_matrix,
    cmap="YlOrRd",
    linewidths=0.5,
    linecolor="white",
    annot=True,
    fmt=".0f",
    cbar_kws={
        "label":"Energy Traded (kWh)"
    }
)

plt.title(
    "Trading Matrix Between Prosumers and Consumers",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Consumers")
plt.ylabel("Prosumers")

plt.tight_layout()

plt.savefig(
    "heatmaps/trading_matrix_heatmap.png",
    dpi=600
)

plt.close()

# ==========================================================
# 2. Adaptive Pricing Behaviour Heatmap
# ==========================================================

micro = pd.read_csv("microgrids.csv")

# Create battery bins
battery_bins = [20,40,60,80,100]
battery_labels = [
    "20-40",
    "40-60",
    "60-80",
    "80-100"
]

micro["Battery Group"] = pd.cut(
    micro["Battery"],
    bins=battery_bins,
    labels=battery_labels,
    include_lowest=True
)

# Create available energy bins
available_bins = np.linspace(
    micro["Available"].min(),
    micro["Available"].max(),
    6
)

micro["Available Group"] = pd.cut(
    micro["Available"],
    bins=available_bins,
    include_lowest=True
)

price_matrix = micro.pivot_table(
    index="Battery Group",
    columns="Available Group",
    values="Price",
    aggfunc="mean",
    observed=False
)

plt.figure(figsize=(10,6))

sns.heatmap(
    price_matrix,
    cmap="coolwarm",
    annot=True,
    fmt=".2f",
    linewidths=0.5,
    linecolor="white",
    cbar_kws={
        "label":"Adaptive Price (ETK/kWh)"
    }
)

plt.title(
    "Adaptive Pricing Behaviour",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Available Energy (kWh)")
plt.ylabel("Battery Level (%)")

plt.tight_layout()

plt.savefig(
    "heatmaps/pricing_heatmap.png",
    dpi=600
)

plt.close()

# ==========================================================
# 3. 24-Hour Operational Heatmap
# ==========================================================

hourly = pd.read_csv("hourly_microgrid.csv")

hourly_matrix = hourly[
    [
        "Generation",
        "Demand",
        "Battery",
        "Available",
        "Price",
        "Energy Traded"
    ]
].T

plt.figure(figsize=(12,5))

sns.heatmap(
    hourly_matrix,
    cmap="viridis",
    linewidths=0.4,
    linecolor="white",
    xticklabels=hourly["Hour"],
    yticklabels=[
        "Generation",
        "Demand",
        "Battery",
        "Available",
        "Price",
        "Energy Traded"
    ],
    cbar_kws={
        "label":"Magnitude"
    }
)

plt.title(
    "24-Hour Operational Behaviour",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Hour of Day")
plt.ylabel("Parameters")

plt.tight_layout()

plt.savefig(
    "heatmaps/24hr_heatmap.png",
    dpi=600
)

plt.close()

print("="*60)
print("Heatmaps Generated Successfully")
print("="*60)
