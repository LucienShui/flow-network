#ifndef NETWORK_FLOWS_FLOW_NETWORK_H
#define NETWORK_FLOWS_FLOW_NETWORK_H

#include <cstring>
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

            explicit Graph(int n) : cnt(0), head(new int[n]) {
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
        };

        /**
         * 费用流 DAG
         */
        struct Graph {

            int cnt, n, m, *head;
            Edge *edge;

            explicit Graph(int n, int m) : cnt(0), n(n), m(m), head(new int[n]), edge(new Edge[m]) {
                memset(head, 0xff, sizeof(int) * n);
            }

            void add_edge(int u, int v, int flow, int cost) {
                edge[cnt] = {head[u], u, v, flow, cost};
                head[u] = cnt++;
                edge[cnt] = {head[v], v, u, 0, -cost};
                head[v] = cnt++;
            }
        };
    }

    /**
     * 网络流
     */
    struct FlowNetwork {

        int *dist, *cur, n;
        flow_network::Graph graph;

        explicit FlowNetwork(int n);

        bool bfs(int S, int T);

        int dfs(int u, int T, int low = INF);

        int run(int S, int T);
    };

    /**
     * 费用流
     */
    struct MinimumCostFlow {

        int *dist, *pre, *low, *vis, *que, clk, n, m, size_of_array;
        minimum_cost_flow::Graph graph;

        explicit MinimumCostFlow(int n, int m);

        bool bfs(int S, int T);

        std::pair<int, int> run(int S, int T);
    };
}

#endif //NETWORK_FLOWS_FLOW_NETWORK_H
