import { useState } from "react";
import { ethers } from "ethers";
import { useWallet } from "../../hooks/useWallet";

function BuyEnergy({ offer, onSuccess }) {
    const { marketplace, energyToken } = useWallet();
    const [amount, setAmount] = useState("");
    const handleBuy = async () => {
        if (!amount || Number(amount) <= 0) {
            alert("Enter a valid amount.");
            return;
        }
        try {
            const energyAmount = Number(amount);
            const totalCost =
                energyAmount * Number(offer.sellingPrice);
            // Approve ETK
            const approveTx = await energyToken.approve(
                marketplace.target,
                ethers.parseUnits(totalCost.toString(), 18)
            );

            await approveTx.wait();
            // Buy Energy
            const buyTx = await marketplace.buyEnergy(
                offer.offerId,
                energyAmount
            );
            await buyTx.wait();
            alert("Energy purchased successfully!");
            setAmount("");
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
        <div className="flex gap-2 mt-3">
            <input
                type="number"
                placeholder="kWh"
                value={amount}
                onChange={(e)=>setAmount(e.target.value)}
                className="bg-slate-700 rounded px-3 py-2 w-28"
            />
            <button
                onClick={handleBuy}
                className="bg-green-600 px-4 rounded"
            >
                Buy
            </button>
        </div>
    );
}

export default BuyEnergy;