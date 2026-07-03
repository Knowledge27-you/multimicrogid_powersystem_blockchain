import Layout from "../components/layout/Layout";

import DashboardHeader from "../components/dashboard/DashboardHeader";
import DashboardCards from "../components/dashboard/DashboardCards";
import RegisterMicrogrid from "../components/dashboard/RegisterMicrogrid";
import MyMicrogrid from "../components/dashboard/MyMicrogrid";
import UpdateStatus from "../components/dashboard/UpdateStatus";

import { useState } from "react";

function Dashboard() {

    const [refresh, setRefresh] = useState(0);

    return (
        <div className="px-5 bg-slate-900">
            <Layout>
                <div className="ml-64 mt-20">
                    <DashboardHeader />
                    <DashboardCards />

                    <div className="grid grid-cols-2 gap-6">
                        <MyMicrogrid refresh={refresh} />
                        <RegisterMicrogrid onSuccess={() => setRefresh(prev => prev + 1)} />
                    </div>

                    <div className="mt-6">
                        <UpdateStatus onSuccess={() => setRefresh(prev => prev + 1)} />
                    </div>
                </div>
            </Layout>
        </div>
    );
}

export default Dashboard;