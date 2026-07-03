import { useState } from "react";
import { useWallet } from "../../hooks/useWallet";

function CreateOffer({ onSuccess }) {

    const { marketplace, registry } = useWallet();

    const [formData, setFormData] = useState({
        energy: "",
        price: "",
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

            // Get the connected user's microgrid
            const grid = await registry.getMyMicrogrid();

            const tx = await marketplace.createOffer(
                Number(grid.id),
                Number(formData.energy),
                Number(formData.price)
            );

            await tx.wait();

            alert("Offer Created Successfully!");

            setFormData({
                energy: "",
                price: "",
            });

            if (onSuccess) onSuccess();

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
                Create Offer
            </h2>

            <form
                onSubmit={handleSubmit}
                className="flex flex-col gap-4"
            >

                <input
                    type="number"
                    name="energy"
                    placeholder="Energy (kWh)"
                    value={formData.energy}
                    onChange={handleChange}
                    className="p-2 rounded bg-slate-700"
                />

                <input
                    type="number"
                    name="price"
                    placeholder="Price (ETK/kWh)"
                    value={formData.price}
                    onChange={handleChange}
                    className="p-2 rounded bg-slate-700"
                />

                <button
                    className="bg-blue-600 p-2 rounded"
                >
                    Create Offer
                </button>

            </form>

        </div>

    );

}

export default CreateOffer;