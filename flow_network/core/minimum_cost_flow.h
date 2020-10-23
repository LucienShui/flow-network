#ifndef NETWORK_FLOWS_FLOW_NETWORK_H
#define NETWORK_FLOWS_FLOW_NETWORK_H

#include "base_network.h"

namespace flow_network {

    /**
     * 费用流
     */
    struct MinimumCostFlow : BaseNetwork {

        int *pre, *low, *vis, clk;

        explicit MinimumCostFlow(int n);

        ~MinimumCostFlow();

        bool bfs(int S, int T);

        std::pair<ll, ll> run(int S, int T);
    };
}

#endif //NETWORK_FLOWS_FLOW_NETWORK_H
