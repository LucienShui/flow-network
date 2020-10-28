#include "graph.h"

namespace flow_network {

    Edge::Edge(int next, int u, int v, int flow, int cost) : next(next), u(u), v(v), flow(flow),
                                                             cost(cost) {}

    Graph::Graph(int n) : cnt(0), head(new int[n]) {
        memset(head, 0xff, sizeof(int) * n);
    }

    Graph::~Graph() {
        delete[] head;
        std::vector<Edge>().swap(edges);
    }

    void Graph::add_edge(int u, int v, int flow, int cost) {
        edges.emplace_back(head[u], u, v, flow, cost);
        head[u] = cnt++;
        edges.emplace_back(head[v], v, u, 0, -cost);
        head[v] = cnt++;
    }
}