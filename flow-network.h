#ifndef NETWORK_FLOWS_FLOW_NETWORK_H
#define NETWORK_FLOWS_FLOW_NETWORK_H

#include <vector>

namespace flow_network {

    const int INF = 0x3f3f3f3f;

    namespace flow_network {

        /**
         * 朴素网络流链式前向星
         */
        struct Edge {
            int next, v, flow;

            Edge(int next, int v, int flow) : next(next), v(v), flow(flow) {}
        };

        /**
         * 朴素网络流 DAG
         */
        struct Graph {

            int cnt, *head;
            std::vector<Edge> edge;

            explicit Graph(int n): cnt(0), head(new int[n]) {
                memset(head, 0xff, sizeof(int) * n);
            }

            void add_edge(int u, int v, int flow) {
                edge.emplace_back(head[u], v, flow);
                head[u] = cnt++;
                edge.emplace_back(head[v], u, 0);
                head[v] = cnt++;
            }
        };

    }

    namespace minimum_cost_flow {

        /**
         * 费用流链式前向星
         */
        struct Edge {
            int next, u, v, flow, cost;

            explicit Edge(int next, int u, int v, int flow, int cost) : next(next), u(u), v(v), flow(flow),
                                                                        cost(cost) {}
        };

        /**
         * 费用流 DAG
         */
        struct Graph {

            int cnt, *head;
            std::vector<Edge> edge;

            explicit Graph(int n): cnt(0), head(new int[n]) {
                memset(head, 0xff, sizeof(int) * n);
            }

            void add_edge(int u, int v, int flow, int cost) {
                edge.emplace_back(head[u], u, v, flow, cost);
                head[u] = cnt++;
                edge.emplace_back(head[v], v, u, 0, -cost);
                head[v] = cnt++;
            }
        };
    }

    /**
     * 网络流
     */
    class FlowNetwork {

        int *dist, *cur, n;
        flow_network::Graph graph;

        explicit FlowNetwork(int n);
    };

    /**
     * 费用流
     */
    class MinimumCostFlow;
}

#endif //NETWORK_FLOWS_FLOW_NETWORK_H
