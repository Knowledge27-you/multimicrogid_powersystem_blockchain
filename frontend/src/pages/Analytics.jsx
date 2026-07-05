import Layout from "../components/layout/Layout";
import systemOverview from "../../../simulations/24hr_graphs/system_overview.png"
import comparison from "../../../simulations/comparison_graphs/figure6_comparison.png"
import systemOverview2 from "../../../simulations/graphs/figure8_system_overview.png"
import analytics from "../assets/analytics.png"

function Analytics() {
    return (
        <div className="px-5 bg-slate-900">
            <Layout>
                <div className="flex flex-col gap-5 ml-64 mt-20 p-5">
                    <h2 className="text-4xl font-bold text-white">Analytics</h2>
                    <div className="h-full w-full flex flex-row gap-8 overflow-auto">
                        <div className="flex flex-col gap-2 justify-center items-center">
                            <img src={systemOverview} className="h-150" alt="systemOverview" />
                            <h2 className="text-teal-400 font-semibold text-lg">System Overview for 24-hrs simulation</h2>
                        </div>
                        <div className="flex flex-col gap-2 justify-center items-center">
                            <img src={comparison} className="h-150" alt="comparison" />
                            <h2 className="text-teal-400 font-semibold text-lg">Comparison between the 3 Pricing System</h2>
                        </div>
                        <div className="flex flex-col gap-2 justify-center items-center">
                            <img src={systemOverview2} className="h-150" alt="systemOverview2" />
                            <h2 className="text-teal-400 font-semibold text-lg">System Overview for all Microgrid simulation</h2>
                        </div>
                    </div>
                    <div className="analytics w-full flex flex-row justify-between items-center">
                        <img src={analytics} alt="analytics" className="h-100"/>
                    </div>
                </div>
            </Layout>
        </div>
    );
}

export default Analytics;