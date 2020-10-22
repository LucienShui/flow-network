#ifndef FLOW_NETWORK_BASE_NETWORK_H
#define FLOW_NETWORK_BASE_NETWORK_H

#include "graph.h"

namespace flow_network {

    struct BaseNetwork {
        int *dist, n;
        Graph graph;

        explicit BaseNetwork(int n);
    };
}

#endif //FLOW_NETWORK_BASE_NETWORK_H
