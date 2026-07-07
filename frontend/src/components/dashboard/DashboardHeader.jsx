import { useWallet } from "../../hooks/useWallet";

function DashboardHeader() {
    const { account } = useWallet();
    return (
        <div className="mb-8">
            <h1 className="text-4xl font-bold">
                Dashboard
            </h1>
            <p className="text-gray-400 mt-2">
                Welcome back
            </p>
            <p className="text-cyan-400">
                {account}
            </p>
        </div>
    );
}

export default DashboardHeader;