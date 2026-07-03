import React from 'react'
import { useNavigate } from "react-router-dom";


const DashboardButton = () => {
    const navigate = useNavigate();
    return (
        <div>
            <button
                onClick={() => navigate("/dashboard")}
                className="bg-emerald-700 
                hover:duration-600 
                hover:ease-in-out
                hover:scale-[0.99] 
                
                text-white px-6 py-3 rounded-lg"
            >
                Go to Dashboard
            </button>
        </div>
    )
}

export default DashboardButton
