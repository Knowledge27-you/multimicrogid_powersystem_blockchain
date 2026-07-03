import { useEffect, useState } from "react";
import { useWallet } from "../../hooks/useWallet";

function MyMicrogrid({refresh}) {

    const { registry, account } = useWallet();

    const [grid, setGrid] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadMicrogrid() {
            if (!registry || !account) return;
            try {
                const data = await registry.getMyMicrogrid();
                setGrid(data);
            } catch (error) {
                console.log(error);
            } finally {
                setLoading(false);
            }
        }
        loadMicrogrid();
    }, [registry, account, refresh]);

    if (loading) {
        return <p>Loading...</p>;
    }
    if (!grid) {
        return (
            <div className="bg-slate-800 p-6 rounded-lg">
                <h2 className="text-2xl font-bold mb-3">
                    My Microgrid
                </h2>

                <p>No microgrid registered.</p>
            </div>
        );
    }

    return (
        <div className="bg-slate-800 p-6 rounded-lg">
            <h2 className="text-2xl font-bold mb-4">
                My Microgrid
            </h2>

            <p><strong>Name:</strong> {grid.name}</p>
            <p><strong>Owner:</strong> {grid.owner}</p>
            <p><strong>Generation:</strong> {grid.energyGenerated.toString()} kWh</p>
            <p><strong>Demand:</strong> {grid.energyDemand.toString()} kWh</p>
            <p><strong>Battery:</strong> {grid.batteryLevel.toString()} %</p>
            <p><strong>Capacity:</strong> {grid.maxCapacity.toString()} kWh</p>
            <p><strong>Reserved:</strong> {grid.reservedEnergy.toString()} kWh</p>
            <p><strong>Status:</strong> {grid.isActive ? "Active" : "Inactive"}</p>
        </div>
    );
}

export default MyMicrogrid;