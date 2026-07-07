import copy
import pandas as pd

from simulation import (
    generate_microgrids,
    execute_trades,
    adaptive_price,
    fixed_price,
    demand_based_price
)

def evaluate(name, grids, pricing):

    grids = copy.deepcopy(grids)
    initial_grids = copy.deepcopy(grids)

    trades = execute_trades(grids, pricing)

    total_energy = sum(t.energy for t in trades)

    total_etk = sum(t.total_cost for t in trades)

    avg_price = (
        total_etk / total_energy
        if total_energy else 0
    )

    surplus = 0
    deficit = 0

    for g in initial_grids:

        available = g.generated_energy - g.demanded_energy

        if available > 0:
            surplus += available
        else:
            deficit += abs(available)

    utilization = (
        total_energy / surplus * 100
        if surplus else 0
    )

    satisfaction = (
        total_energy / deficit * 100
        if deficit else 0
    )

    satisfaction = min(satisfaction, 100)

    efficiency = (
        total_energy /
        min(surplus, deficit)
        * 100
        if min(surplus, deficit) > 0 else 0
    )

    efficiency = min(efficiency, 100)

    return {

        "Strategy": name,

        "Trades": len(trades),

        "Energy Traded": total_energy,

        "Average Price": round(avg_price,2),

        "Total ETK": total_etk,

        "Prosumer Utilization": round(utilization,2),

        "Consumer Satisfaction": round(satisfaction,2),

        "Market Efficiency": round(efficiency,2)

    }

def main():

    grids = generate_microgrids(50)

    results = [

        evaluate(
            "Fixed Pricing",
            grids,
            fixed_price
        ),

        evaluate(
            "Demand Pricing",
            grids,
            demand_based_price
        ),

        evaluate(
            "Adaptive Pricing",
            grids,
            adaptive_price
        )

    ]

    df = pd.DataFrame(results)

    print(df)

    df.to_csv(
        "comparison_results.csv",
        index=False
    )


if __name__ == "__main__":
    main()
