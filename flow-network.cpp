#include "flow-network.h"

#include <map>
#include <queue>

namespace flow_network {

    /**
     * 朴素网络流
     */
    struct FlowNetwork {

        int *dist, *cur, n;
        flow_network::Graph graph;

        explicit FlowNetwork(int n) : graph(n), n(n), dist(new int[n]), cur(new int[n]) {}

        bool bfs(int S, int T) {
            memset(dist, 0xff, sizeof(int) * n);
            dist[S] = 0;
            std::queue<int> que;
            que.push(S);
            while (!que.empty()) {
                int u = que.front();
                que.pop();
                for (int i = graph.head[u]; ~i; i = graph.edge[i].next) {
                    int v = graph.edge[i].v, flow = graph.edge[i].flow;
                    if (dist[v] == -1 && flow > 0) {
                        dist[v] = dist[u] + 1;
                        if (v == T) return true;
                        que.push(v);
                    }
                }
            }
            return false;
        }

        int dfs(int u, int T, int low = INF) {
            if (u == T) return low;
            for (int &i = cur[u]; ~i; i = graph.edge[i].next) {
                int v = graph.edge[i].v, flow = graph.edge[i].flow;
                if (dist[v] == dist[u] + 1 && flow > 0) {
                    int min = dfs(v, flow < low ? flow : low, T);
                    if (min > 0) {
                        graph.edge[i].flow -= min;
                        graph.edge[i ^ 1].flow += min;
                        return min;
                    }
                }
            }
            return 0;
        }

        int run(int S, int T) {
            int ans = 0, tmp;
            while (bfs(S, T)) {
                memcpy(cur, graph.head, sizeof(int) * n);
                while (tmp = dfs(S, T), tmp > 0) ans += tmp;
            }
            return ans;
        }
    };

    /**
     * 费用流
     */
    struct MinimumCostFlow {

        int *dist, *pre, *low, *vis, clk, n;
        minimum_cost_flow::Graph graph;

        explicit MinimumCostFlow(int n) : graph(n), n(n), dist(new int[n]), pre(new int[n]), low(new int[n]),
                                          vis(new int[n]), clk(0) {}

        bool bfs(int S, int T) {
            vis[S] = ++clk, low[S] = INF, memset(dist, 0x3f, sizeof(int) * n), dist[S] = 0;
            std::queue<int> que;
            que.push(S);
            while (!que.empty()) {
                int u = que.front();
                que.pop();
                vis[u] = -1;
                for (int i = graph.head[u]; ~i; i = graph.edge[i].next) {
                    int v = graph.edge[i].v, flow = graph.edge[i].flow, cost = graph.edge[i].cost;
                    if (dist[v] > dist[u] + cost && flow > 0) {
                        dist[v] = dist[u] + cost;
                        pre[v] = i;
                        low[v] = std::min(low[u], flow);
                        if (vis[v] != clk) {
                            que.push(v);
                            vis[v] = clk;
                        }
                    }
                }
            }
            return dist[T] < INF;
        }

        std::pair<int, int> run(int S, int T) {
            int flow = 0, cost = 0;
            while (bfs(S, T)) {
                flow += low[T];
                cost += low[T] * dist[T];
                for (int u = T; u != S; u = graph.edge[pre[u]].u) {
                    graph.edge[pre[u]].flow -= low[T];
                    graph.edge[pre[u] ^ 1].flow += low[T];
                }
            }
            return std::make_pair(flow, cost);
        }
    };
}
