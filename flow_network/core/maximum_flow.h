#ifndef FLOW_NETWORK_MAXIMUM_FLOW_H
#define FLOW_NETWORK_MAXIMUM_FLOW_H

#include "base_network.h"

namespace flow_network {

    /**
     * 最大流
     */
    struct MaximumFlow : BaseNetwork {

        int *cur;

        explicit MaximumFlow(int n);

        ~MaximumFlow();

        bool bfs(int S, int T);

        int dfs(int u, int T, int low = INF);

        int run(int S, int T);
    };

}

#endif //FLOW_NETWORK_MAXIMUM_FLOW_H
