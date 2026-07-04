import random as r
from dataclasses import dataclass
import pandas as pd

r.seed(42)  # For reproducibility
# pricing constants

BASE_PRICE = 10

HIGH_SURPLUS_DISC = 2
MID_SURPLUS_DISC = 1

LOW_SURPLUS_PREMIUM = 2
DEFICIT_SURPLUS_PREMIUM = 4

HIGH_BATTERY_DISC = 2
MID_BATTERY_DISC = 1

LOW_BATTERY_PREMIUM = 2
DEFICIT_BATTERY_PREMIUM = 4

MAX_CAPACITY = 1000

# microgrid

@dataclass
class Microgrid:
    id: int
    generated_energy: int
    demanded_energy: int
    battery_level: int
    max_capacity: int = MAX_CAPACITY
    reserved_energy: int = 0

@dataclass
class Trade:
    prosumer: int
    consumer: int
    energy: int
    price: float
    total_cost: float

def generate_microgrids(count):

    grids = []

    for i in range(1, count + 1):

        generation = r.randint(200, 1000)

        demand = r.randint(100, 900)

        battery = r.randint(20, 100)

        grids.append(

            Microgrid(

                id=i,
                generated_energy=generation,
                demanded_energy=demand,
                battery_level=battery

            )

        )

    return grids

def calculate_price(generated_energy, demanded_energy, battery_level, max_capacity, reserved_energy):

    price = BASE_PRICE

    available_energy = generated_energy + battery_level - reserved_energy
    availability_ratio = (available_energy * 100) / max_capacity

    if availability_ratio >= 70:
        price -= HIGH_SURPLUS_DISC

    elif availability_ratio >= 40:
        price -= MID_SURPLUS_DISC

    elif availability_ratio >= 20:
        pass

    elif availability_ratio >= 0:
        price += LOW_SURPLUS_PREMIUM

    else:
        price += DEFICIT_SURPLUS_PREMIUM


    # Battery Adjustment

    if battery_level >= 80:
        price -= HIGH_BATTERY_DISC

    elif battery_level >= 60:
        price -= MID_BATTERY_DISC

    elif battery_level >= 40:
        pass

    elif battery_level >= 20:
        price += LOW_BATTERY_PREMIUM

    else:
        price += DEFICIT_BATTERY_PREMIUM


    return max(price, 1)

def export_microgrids(grids):
    rows = []

    for g in grids:
        available = g.generated_energy - g.demanded_energy
        role = "Prosumer" if available > 0 else "Consumer"

        price = calculate_price(
            g.generated_energy,
            g.demanded_energy,
            g.battery_level,
            g.max_capacity,
            g.reserved_energy
        )

        rows.append({
            "ID": g.id,
            "Generation": g.generated_energy,
            "Demand": g.demanded_energy,
            "Battery": g.battery_level,
            "Available": available,
            "Price": price,
            "Role": role
        })
    df = pd.DataFrame(rows)
    df.to_csv("microgrids.csv", index=False)
    return df

def execute_trades(grids):
    prosumers = []
    consumers = []

    for g in grids:

        available = g.generated_energy - g.demanded_energy

        if available > 0:

            prosumers.append({
                "grid": g,
                "available": available
            })

        elif available < 0:

            consumers.append({
                "grid": g,
                "required": abs(available)
            })

    trades = []

    for p in prosumers:

        for c in consumers:

            if p["available"] == 0:
                break

            if c["required"] == 0:
                continue

            traded = min(
                p["available"],
                c["required"]
            )

            price = calculate_price(
                p["grid"].generated_energy,
                p["grid"].demanded_energy,
                p["grid"].battery_level,
                p["grid"].max_capacity,
                p["grid"].reserved_energy
            )

            trades.append(

                Trade(

                    prosumer=p["grid"].id,
                    consumer=c["grid"].id,
                    energy=traded,
                    price=price,
                    total_cost=traded * price

                )

            )

            # Update simulation state
            p["available"] -= traded
            c["required"] -= traded

            # Reflect energy transfer
            p["grid"].generated_energy -= traded
            c["grid"].generated_energy += traded

    return trades

def export_trades(trades):
    rows = []
    for t in trades:
        rows.append({
            "Prosumer": t.prosumer,
            "Consumer": t.consumer,
            "Energy Traded": t.energy,
            "Price": t.price,
            "Total ETK": t.total_cost
        })
    df = pd.DataFrame(rows)
    df.to_csv(
        "simulation_results.csv",
        index=False
    )
    return df

def main():
    NUM_MICROGRIDS = 30
    grids = generate_microgrids(NUM_MICROGRIDS)

    microgrid_df = export_microgrids(grids)
    trades = execute_trades(grids)
    trades_df = export_trades(trades)

    print("Microgrid DataFrame:")
    print(microgrid_df)
    print("Trade DataFrame:")
    print(trades_df)

if __name__ == "__main__":
    main()