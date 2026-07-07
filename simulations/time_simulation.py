import math
import random
import pandas as pd

random.seed(42)

# -----------------------------
# Pricing Function
# -----------------------------

BASE_PRICE = 10

def adaptive_price(generation, demand, battery):

    available = generation - demand

    price = BASE_PRICE

    # Available Energy
    if available >= 500:
        price -= 2
    elif available >= 200:
        price -= 1
    elif available < 0:
        price += 2

    # Battery
    if battery >= 80:
        price -= 2
    elif battery >= 60:
        price -= 1
    elif battery < 20:
        price += 4
    elif battery < 40:
        price += 2

    return max(price,1)

# -----------------------------
# Hourly Simulation
# -----------------------------

battery = 50

rows = []

for hour in range(24):

    # -------------------------
    # PV Generation
    # -------------------------

    if 6 <= hour <= 18:

        generation = int(
            800 *
            math.sin(
                math.pi *
                (hour-6)/12
            )
        )

    else:

        generation = 0

    generation = max(generation,0)

    # -------------------------
    # Load Demand
    # -------------------------

    if hour <= 5:

        demand = random.randint(180,260)

    elif hour <= 9:

        demand = random.randint(300,420)

    elif hour <= 16:

        demand = random.randint(250,350)

    else:

        demand = random.randint(450,700)

    # -------------------------
    # Battery
    # -------------------------

    if generation > demand:

        battery = min(
            100,
            battery + 5
        )

    else:

        battery = max(
            20,
            battery - 4
        )

    # -------------------------
    # Available Energy
    # -------------------------

    available = generation - demand

    # -------------------------
    # Adaptive Price
    # -------------------------

    price = adaptive_price(
        generation,
        demand,
        battery
    )

    # -------------------------
    # Energy Traded
    # -------------------------

    traded = max(
        0,
        available
    )

    rows.append({

        "Hour":hour,

        "Generation":generation,

        "Demand":demand,

        "Battery":battery,

        "Available":available,

        "Price":price,

        "Energy Traded":traded

    })

df = pd.DataFrame(rows)

df.to_csv(
    "hourly_microgrid.csv",
    index=False
)

print(df)

print("\n24-hour simulation completed.")