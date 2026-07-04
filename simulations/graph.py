import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

microgrids = pd.read_csv("microgrids.csv")
trades = pd.read_csv("simulation_results.csv")

# ---------------------------------------------------
# Graph 1
# Energy Generation Distribution
# ---------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    microgrids["Generation"],
    bins=10,
    edgecolor="black"
)

plt.title("Energy Generation Distribution")
plt.xlabel("Energy Generated (kWh)")
plt.ylabel("Number of Microgrids")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph1_generation_distribution.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------
# Graph 2
# Generation vs Demand
# ---------------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    microgrids["Generation"],
    microgrids["Demand"]
)

plt.title("Generation vs Demand")
plt.xlabel("Generation (kWh)")
plt.ylabel("Demand (kWh)")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph2_generation_vs_demand.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------
# Graph 3
# Adaptive Price Distribution
# ---------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    microgrids["Price"],
    bins=8,
    edgecolor="black"
)

plt.title("Adaptive Price Distribution")
plt.xlabel("Price (ETK/kWh)")
plt.ylabel("Frequency")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph3_price_distribution.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------
# Graph 4
# Trade Size Distribution
# ---------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    trades["Energy Traded"],
    bins=10,
    edgecolor="black"
)

plt.title("Trade Size Distribution")
plt.xlabel("Energy Traded (kWh)")
plt.ylabel("Frequency")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph4_trade_distribution.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------
# Graph 5
# Prosumer vs Consumer
# ---------------------------------------------------

prosumer_count = len(
    microgrids[
        microgrids["Role"]=="Prosumer"
    ]
)

consumer_count = len(
    microgrids[
        microgrids["Role"]=="Consumer"
    ]
)

plt.figure(figsize=(6,6))

plt.pie(
    [prosumer_count,consumer_count],
    labels=["Prosumer","Consumer"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Prosumer vs Consumer Ratio")

plt.tight_layout()

plt.savefig(
    "graph5_roles.png",
    dpi=300
)

plt.close()

# ---------------------------------------------------
# Graph 6
# Top 10 Trades
# ---------------------------------------------------

top = trades.sort_values(
    "Energy Traded",
    ascending=False
).head(10)

plt.figure(figsize=(9,5))

plt.bar(
    range(len(top)),
    top["Energy Traded"]
)

plt.xticks(
    range(len(top)),
    top["Prosumer"].astype(str)+"→"+top["Consumer"].astype(str),
    rotation=45
)

plt.ylabel("Energy (kWh)")
plt.title("Top 10 Energy Trades")

plt.tight_layout()

plt.savefig(
    "graph6_top_trades.png",
    dpi=300
)

plt.close()

#---------------------------------------------------
# Trading Price vs Energy Demand (Scatter)
#---------------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    microgrids["Demand"],
    microgrids["Price"],
    alpha=0.7
)

plt.xlabel("Energy Demand (kWh)")
plt.ylabel("Trading Price (ETK/kWh)")
plt.title("Trading Price vs Energy Demand")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph7_price_vs_demand.png",
    dpi=300
)

plt.close()

#---------------------------------------------------
# Trading Price vs Available Energy (Scatter)
#---------------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    microgrids["Available"],
    microgrids["Price"],
    alpha=0.7
)

plt.xlabel("Available Energy (kWh)")
plt.ylabel("Trading Price (ETK/kWh)")
plt.title("Trading Price vs Available Energy")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph8_price_vs_available.png",
    dpi=300
)

plt.close()

#---------------------------------------------------
# Battery Level vs Trading Price (Scatter)
#---------------------------------------------------

plt.figure(figsize=(8,5))

plt.scatter(
    microgrids["Battery"],
    microgrids["Price"],
    alpha=0.7
)

plt.xlabel("Battery Level (%)")
plt.ylabel("Trading Price (ETK/kWh)")
plt.title("Trading Price vs Battery Level")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph9_price_vs_battery.png",
    dpi=300
)

plt.close()

#---------------------------------------------------
# Available Energy vs Battery Level (Colored by Price)
#---------------------------------------------------

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    microgrids["Available"],
    microgrids["Battery"],
    c=microgrids["Price"],
    cmap="viridis",
    s=80
)

plt.xlabel("Available Energy (kWh)")
plt.ylabel("Battery Level (%)")
plt.title("Battery Level and Available Energy vs Trading Price")

plt.colorbar(scatter, label="Trading Price (ETK/kWh)")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph10_battery_available_price.png",
    dpi=300
)

plt.close()

#---------------------------------------------------
# Battery Level vs Available Energy (Prosumer vs Consumer)
#---------------------------------------------------

colors = microgrids["Role"].map({
    "Prosumer": "green",
    "Consumer": "red"
})

plt.figure(figsize=(8,6))

plt.scatter(
    microgrids["Available"],
    microgrids["Battery"],
    c=colors,
    alpha=0.8
)

plt.xlabel("Available Energy (kWh)")
plt.ylabel("Battery Level (%)")
plt.title("Prosumer and Consumer Distribution")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "graph11_role_distribution.png",
    dpi=300
)

plt.close()

print("All graphs generated successfully.")