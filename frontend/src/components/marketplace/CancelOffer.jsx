import { useWallet } from "../../hooks/useWallet";

function CancelOffer({ offerId, onSuccess }) {
    const { marketplace } = useWallet();
    const cancel = async () => {
        try {
            const tx = await marketplace.cancelOffer(
                offerId
            );
            await tx.wait();
            alert("Offer cancelled.");
            if(onSuccess) onSuccess();
        } catch(error){
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
        <button
            onClick={cancel}
            className="bg-red-600 px-4 py-2 rounded mt-3"
        >
            Cancel
        </button>

    );

}

export default CancelOffer;