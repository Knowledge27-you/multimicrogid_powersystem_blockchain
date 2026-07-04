import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("24hr_graphs",exist_ok=True)

df = pd.read_csv("hourly_microgrid.csv")

# ------------------------------------
# Graph Helper
# ------------------------------------

def make_graph(column,title,ylabel,filename,color):

    plt.figure(figsize=(10,4))

    plt.plot(
        df["Hour"],
        df[column],
        linewidth=2.5,
        marker="o",
        color=color
    )

    plt.xticks(range(24))

    plt.grid(True,linestyle="--",alpha=.5)

    plt.title(title)

    plt.xlabel("Hour")

    plt.ylabel(ylabel)

    plt.tight_layout()

    plt.savefig(
        f"24hr_graphs/{filename}",
        dpi=600
    )

    plt.close()

# ------------------------------------

make_graph(
    "Generation",
    "24-Hour PV Generation",
    "kWh",
    "generation.png",
    "tab:blue"
)

make_graph(
    "Demand",
    "24-Hour Load Demand",
    "kWh",
    "demand.png",
    "tab:red"
)

make_graph(
    "Battery",
    "Battery State of Charge",
    "%",
    "battery.png",
    "tab:green"
)

make_graph(
    "Available",
    "Available Energy",
    "kWh",
    "available.png",
    "tab:purple"
)

make_graph(
    "Price",
    "Adaptive Trading Price",
    "ETK",
    "price.png",
    "tab:orange"
)

make_graph(
    "Energy Traded",
    "Energy Traded",
    "kWh",
    "trade.png",
    "tab:brown"
)

# ------------------------------------
# Combined Figure
# ------------------------------------

fig,axs=plt.subplots(
    6,
    1,
    figsize=(10,13),
    sharex=True
)

colors=[
    "tab:blue",
    "tab:red",
    "tab:green",
    "tab:purple",
    "tab:orange",
    "tab:brown"
]

columns=[
    "Generation",
    "Demand",
    "Battery",
    "Available",
    "Price",
    "Energy Traded"
]

titles=[
    "(a) PV Generation",
    "(b) Load Demand",
    "(c) Battery SOC",
    "(d) Available Energy",
    "(e) Adaptive Price",
    "(f) Energy Traded"
]

for ax,col,title,color in zip(
    axs,
    columns,
    titles,
    colors
):

    ax.plot(
        df["Hour"],
        df[col],
        color=color,
        linewidth=2.5,
        marker="o",
        markersize=4
    )

    ax.grid(
        True,
        linestyle="--",
        alpha=.5
    )

    ax.set_title(title)

axs[-1].set_xlabel("Hour of the Day")

plt.tight_layout()

plt.savefig(
    "24hr_graphs/system_overview.png",
    dpi=600
)

plt.close()

print("All 24-hour graphs generated.")