import { useState } from "react";
import { useWallet } from "../../hooks/useWallet";

function UpdateStatus({onSuccess}) {

    const { registry } = useWallet();

    const [formData, setFormData] = useState({
        generation: "",
        demand: "",
        battery: "",
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {

            const tx = await registry.updateStatus(
                Number(formData.generation),
                Number(formData.demand),
                Number(formData.battery)
            );

            await tx.wait();

            if(onSuccess){
                onSuccess();
            }

            alert("Status updated successfully!");

            setFormData({
                generation: "",
                demand: "",
                battery: "",
            });

        } catch (error) {
            console.error(error);
            alert(
                error.reason ||
                error.data?.message ||
                error.error?.message ||
                error.message
            );
        }
    };

    return (
        <div className="bg-slate-800 p-6 rounded-lg">

            <h2 className="text-xl font-bold mb-4">
                Update Status
            </h2>

            <form
                onSubmit={handleSubmit}
                className="flex flex-col gap-4"
            >

                <input
                    type="number"
                    name="generation"
                    placeholder="Energy Generated"
                    value={formData.generation}
                    onChange={handleChange}
                    className="p-2 rounded text-white bg-slate-700"
                />

                <input
                    type="number"
                    name="demand"
                    placeholder="Energy Demand"
                    value={formData.demand}
                    onChange={handleChange}
                    className="p-2 rounded text-white bg-slate-700"
                />

                <input
                    type="number"
                    name="battery"
                    placeholder="Battery Level (%)"
                    value={formData.battery}
                    onChange={handleChange}
                    className="p-2 rounded text-white bg-slate-700"
                />

                <button
                    className="bg-blue-600 hover:bg-blue-700 p-2 rounded"
                >
                    Update Status
                </button>

            </form>

        </div>
    );
}

export default UpdateStatus;