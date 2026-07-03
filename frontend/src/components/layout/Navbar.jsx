import { useWallet } from "../../hooks/useWallet";

function Navbar() {
    const { account } = useWallet();
    return (
        <nav className="h-16 bg-slate-900 border-b border-slate-700 flex items-center justify-between px-8">
            <h1 className="text-xl font-bold text-cyan-400">
                ⚡ Energy Trading
            </h1>
            <div className="text-sm text-white">
                {
                    account
                        ? `${account.slice(0, 6)}...${account.slice(-4)}`
                        : "Wallet Not Connected"
                }
            </div>
        </nav>
    );
}

export default Navbar;