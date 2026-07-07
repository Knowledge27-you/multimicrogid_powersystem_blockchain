function StatCard({ title, value, unit }) {

    return (
        <div className="bg-slate-900 rounded-xl p-6 border border-slate-700">
            <p className="text-gray-400">
                {title}
            </p>
            <h2 className="text-3xl font-bold mt-2">
                {value}
                <span className="text-lg text-gray-400 ml-2">
                    {unit}
                </span>
            </h2>
        </div>
    );
}

export default StatCard;