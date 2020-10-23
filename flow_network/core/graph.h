#ifndef FLOW_NETWORK_GRAPH_H
#define FLOW_NETWORK_GRAPH_H

#include "common.h"
#include <cstring>
#include <vector>

namespace flow_network {

    /**
     * 费用流链式前向星
     */
    struct Edge {
        int next, u, v, flow, cost;

        Edge() = default;

        Edge(int next, int u, int v, int flow, int cost);
    };

    /**
     * 费用流 DAG
     */
    struct Graph {

        int cnt, *head;
        std::vector<Edge> edges;

        explicit Graph(int n);

        ~Graph();

        void add_edge(int u, int v, int flow, int cost = 0);
    };
}

#endif //FLOW_NETWORK_GRAPH_H
