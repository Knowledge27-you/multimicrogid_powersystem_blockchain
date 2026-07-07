import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("graphs", exist_ok=True)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

microgrids = pd.read_csv("microgrids.csv")
trades = pd.read_csv("simulation_results.csv")

# ---------------------------------------------------
# Graph 1
# Energy Generation Profile
# ---------------------------------------------------

plt.figure(figsize=(10,4))

df = microgrids.sort_values(
    by="Available",
    ascending=False
).reset_index(drop=True)

plt.plot(
    range(1, len(df) + 1),
    df["Generation"],
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.title("Energy Generation Profile")
plt.xlabel("Sorted Microgrids")
plt.ylabel("Generation (kWh)")

plt.grid(True, linestyle="--", alpha=.6)

plt.tight_layout()

plt.savefig("graphs/figure1_generation_profile.png",dpi=600)

plt.close()

# ---------------------------------------------------
# Graph 2
# Load Demand Profile
# ---------------------------------------------------

plt.figure(figsize=(10,4))

plt.plot(
    range(1, len(df) + 1),
    df["Demand"],
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.title("Load Demand Profile")

plt.xlabel("Sorted Microgrids")

plt.ylabel("Demand (kWh)")

plt.grid(True,linestyle="--",alpha=.6)

plt.tight_layout()

plt.savefig("graphs/figure2_demand_profile.png",dpi=600)

plt.close()

# ---------------------------------------------------
# Graph 3
# Battery State of Charge
# ---------------------------------------------------

plt.figure(figsize=(10,4))

plt.plot(
    range(1, len(df) + 1),
    df["Battery"],
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.title("Battery State of Charge (SOC)")

plt.xlabel("Sorted Microgrids")

plt.ylabel("Battery SOC (%)")

plt.grid(True,linestyle="--",alpha=.6)

plt.tight_layout()

plt.savefig("graphs/figure3_battery_soc.png",dpi=600)

plt.close()

# ---------------------------------------------------
# Graph 4
# Available Energy Distribution
# ---------------------------------------------------

plt.figure(figsize=(10,4))

plt.plot(
    range(1, len(df) + 1),
    df["Available"],
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.axhline(0,color="red",linestyle="--")

plt.title("Available Energy Across Microgrids")

plt.xlabel("Sorted Microgrids")

plt.ylabel("Available Energy (kWh)")

plt.grid(True,linestyle="--",alpha=.6)

plt.tight_layout()

plt.savefig("graphs/figure4_available_energy.png",dpi=600)

plt.close()

# ---------------------------------------------------
# Graph 5
# Adaptive Trading Price
# ---------------------------------------------------

plt.figure(figsize=(10,4))

plt.plot(
    range(1, len(df) + 1),
    df["Price"],
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.title("Adaptive Trading Price")

plt.xlabel("Sorted Microgrids")

plt.ylabel("Trading Price (ETK/kWh)")

plt.grid(True,linestyle="--",alpha=.6)

plt.tight_layout()

plt.savefig("graphs/figure5_adaptive_price.png",dpi=600)

plt.close()

# ---------------------------------------------------
# Graph 6
# Energy Traded
# ---------------------------------------------------

plt.figure(figsize=(10,4))

trade = trades.reset_index(drop=True)

plt.plot(
    trade.index+1,
    trade["Energy Traded"],
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.title("Energy Traded Per Transaction")

plt.xlabel("Trade Number")

plt.ylabel("Energy (kWh)")

plt.grid(True,linestyle="--",alpha=.6)

plt.tight_layout()

plt.savefig("graphs/figure6_energy_traded.png",dpi=600)

plt.close()

#---------------------------------------------------
# Graph 7
# ETK Transaction Value
#---------------------------------------------------

plt.figure(figsize=(10,4))

plt.plot(
    trade.index+1,
    trade["Total ETK"],
    linewidth=2.5,
    marker="o",
    markersize=4
)

plt.title("Transaction Value")

plt.xlabel("Trade Number")

plt.ylabel("ETK")

plt.grid(True,linestyle="--",alpha=.6)

plt.tight_layout()

plt.savefig("graphs/figure7_trade_value.png",dpi=600)

plt.close()

#---------------------------------------------------
# Graph 8
# System Overview
#---------------------------------------------------

fig, axs = plt.subplots(
    5,
    1,
    figsize=(10, 12),
    sharex=True
)

# Generation
axs[0].plot(
    range(1, len(df)+1),
    df["Generation"],
    color="tab:blue",
    linewidth=2.5
)
axs[0].set_ylabel("kWh")
axs[0].set_title("(a) Energy Generation", fontsize=11)
axs[0].grid(True, linestyle="--", alpha=0.5)

# Demand
axs[1].plot(
    range(1, len(df)+1),
    df["Demand"],
    color="tab:red",
    linewidth=2.5
)
axs[1].set_ylabel("kWh")
axs[1].set_title("(b) Energy Demand", fontsize=11)
axs[1].grid(True, linestyle="--", alpha=0.5)

# Battery SOC
axs[2].plot(
    range(1, len(df)+1),
    df["Battery"],
    color="tab:green",
    linewidth=2.5
)
axs[2].set_ylabel("%")
axs[2].set_title("(c) Battery State of Charge (SOC)", fontsize=11)
axs[2].grid(True, linestyle="--", alpha=0.5)

# Available Energy
axs[3].plot(
    range(1, len(df)+1),
    df["Available"],
    color="tab:purple",
    linewidth=2.5
)
axs[3].axhline(0, color="black", linestyle="--", linewidth=1)
axs[3].set_ylabel("kWh")
axs[3].set_title("(d) Available Energy", fontsize=11)
axs[3].grid(True, linestyle="--", alpha=0.5)

# Adaptive Price
axs[4].plot(
    range(1, len(df)+1),
    df["Price"],
    color="tab:orange",
    linewidth=2.5
)
axs[4].set_ylabel("ETK")
axs[4].set_xlabel("Sorted Microgrids")
axs[4].set_title("(e) Adaptive Trading Price", fontsize=11)
axs[4].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "graphs/figure8_system_overview.png",
    dpi=600,
    bbox_inches="tight"
)

plt.close()


# comparison graphs
os.makedirs("comparison_graphs", exist_ok=True)

df = pd.read_csv("comparison_results.csv")

#--------------------------------------------
# Number of trades
#--------------------------------------------

plt.figure(figsize=(7,5))

plt.bar(df["Strategy"], df["Trades"])

plt.title("Number of Successful Trades")
plt.ylabel("Trades")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "comparison_graphs/figure1_trades.png",
    dpi=600
)

plt.close()

#--------------------------------------------
# Energy Traded
#--------------------------------------------

plt.figure(figsize=(7,5))

plt.bar(df["Strategy"], df["Energy Traded"])

plt.title("Total Energy Traded")
plt.ylabel("Energy (kWh)")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "comparison_graphs/figure2_energy.png",
    dpi=600
)

plt.close()

#--------------------------------------------
# Average Trading Price
#--------------------------------------------

plt.figure(figsize=(7,5))

plt.bar(df["Strategy"], df["Average Price"])

plt.title("Average Trading Price")
plt.ylabel("ETK / kWh")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "comparison_graphs/figure3_price.png",
    dpi=600
)

plt.close()

#--------------------------------------------
# Total ETK Exchanged
#--------------------------------------------

plt.figure(figsize=(7,5))

plt.bar(df["Strategy"], df["Total ETK"])

plt.title("Total ETK Exchanged")
plt.ylabel("ETK")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "comparison_graphs/figure4_etk.png",
    dpi=600
)

plt.close()

#--------------------------------------------
# Consumer Satisfaction
#--------------------------------------------

plt.figure(figsize=(7,5))

plt.bar(df["Strategy"], df["Consumer Satisfaction"])

plt.title("Consumer Satisfaction")
plt.ylabel("%")
plt.ylim(0,100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "comparison_graphs/figure5_satisfaction.png",
    dpi=600
)

plt.close()

#--------------------------------------------
# Combined Comparision
#--------------------------------------------

fig, axs = plt.subplots(3,2, figsize=(12,10))

metrics = [
    ("Trades","Number of Trades"),
    ("Energy Traded","Energy Traded"),
    ("Average Price","Average Price"),
    ("Total ETK","Total ETK"),
    ("Consumer Satisfaction","Consumer Satisfaction"),
    ("Prosumer Utilization","Prosumer Utilization")
]

for ax, (column, title) in zip(axs.flat, metrics):

    ax.bar(df["Strategy"], df[column])

    ax.set_title(title)

    ax.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "comparison_graphs/figure6_comparison.png",
    dpi=600
)

plt.close()

print("All graphs generated successfully.")