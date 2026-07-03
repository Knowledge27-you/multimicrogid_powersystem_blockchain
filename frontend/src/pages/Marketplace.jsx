import { useState } from "react";

import Layout from "../components/layout/Layout";
import CreateOffer from "../components/marketplace/CreateOffer";
import ActiveOffers from "../components/marketplace/ActiveOffers";

function Marketplace() {

    const [refresh, setRefresh] = useState(0);

    return (
      <div className="bg-slate-900 p-5">
        <Layout>
          <h1 className="text-3xl font-bold mb-6">
            Marketplace
          </h1>
          <CreateOffer
            onSuccess={() => setRefresh(prev => prev + 1)}
          />
          <ActiveOffers
            refresh={refresh}
          />
        </Layout>
      </div>
    );

}

export default Marketplace;