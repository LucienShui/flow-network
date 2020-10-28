#ifndef FLOW_NETWORK_BASE_NETWORK_H
#define FLOW_NETWORK_BASE_NETWORK_H

#include "graph.h"


namespace flow_network {

    struct BaseNetwork {
        int n, *dist;
        Graph graph;

        explicit BaseNetwork(int n);

        ~BaseNetwork();
    };
}

#endif //FLOW_NETWORK_BASE_NETWORK_H
