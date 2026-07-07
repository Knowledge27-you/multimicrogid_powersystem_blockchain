import { useEffect, useState } from "react";
import { useWallet } from "../../hooks/useWallet";
import StatCard from "../common/Statcard";

function DashboardCards({ refresh }) {

    const { registry, account } = useWallet();

    const [stats, setStats] = useState({
        generation: 0,
        demand: 0,
        battery: 0,
        available: 0,
    });

    useEffect(() => {

        async function loadStats() {

            if (!registry || !account) return;

            try {

                const grid = await registry.getMyMicrogrid();
                const available = await registry.getAvailableEnergy(
                    grid.id.toString()
                );

                setStats({
                    generation: Number(grid.energyGenerated),
                    demand: Number(grid.energyDemand),
                    battery: Number(grid.batteryLevel),
                    available: Number(available),
                });

            } catch (error) {

                console.log(error);

            }

        }

        loadStats();

    }, [registry, account, refresh]);

    return (
        <div className="grid grid-cols-4 gap-6 mb-8">

            <StatCard
                title="Generation"
                value={stats.generation}
                unit="kWh"
            />

            <StatCard
                title="Demand"
                value={stats.demand}
                unit="kWh"
            />

            <StatCard
                title="Battery"
                value={stats.battery}
                unit="%"
            />

            <StatCard
                title="Available"
                value={stats.available}
                unit="kWh"
            />

        </div>
    );
}

export default DashboardCards;