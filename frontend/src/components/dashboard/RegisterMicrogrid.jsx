import { useState } from "react";
import { useWallet } from "../../hooks/useWallet";

function RegisterMicrogrid({onSuccess}) {

    const { registry } = useWallet();

    const [formData, setFormData] = useState({
        name: "",
        latitude: "",
        longitude: "",
        maxCapacity: "",
    });

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });

    };

    const registerMicrogrid = async (e) => {

        e.preventDefault();

        try {

            const tx = await registry.registerMicrogrid(

                formData.name,
                Number(formData.latitude),
                Number(formData.longitude),
                Number(formData.maxCapacity)

            );

            await tx.wait();

            if(onSuccess){
                onSuccess();
            }

            alert("Microgrid Registered Successfully!");
        } catch (err) {
            console.error(err);
            alert(err.reason || "Registration Failed");
        }

    };

    return (

        <form
            onSubmit={registerMicrogrid}
            className="bg-slate-800 p-6 rounded-xl flex flex-col gap-4"
        >
            <h2 className="text-2xl font-bold">
                Register Microgrid
            </h2>

            <input
                type="text"
                name="name"
                placeholder="Microgrid Name"
                onChange={handleChange}
                className="p-3 rounded bg-slate-700"
            />

            <input
                type="number"
                name="latitude"
                placeholder="Latitude"
                onChange={handleChange}
                className="p-3 rounded bg-slate-700"
            />

            <input
                type="number"
                name="longitude"
                placeholder="Longitude"
                onChange={handleChange}
                className="p-3 rounded bg-slate-700"
            />

            <input
                type="number"
                name="maxCapacity"
                placeholder="Max Capacity"
                onChange={handleChange}
                className="p-3 rounded bg-slate-700"
            />

            <button
                className="bg-blue-600 p-3 rounded"
            >
                Register
            </button>

        </form>

    );

}

export default RegisterMicrogrid;