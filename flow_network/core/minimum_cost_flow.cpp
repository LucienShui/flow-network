#include "minimum_cost_flow.h"

#include <cstring>
#include <queue>

namespace flow_network {

    MinimumCostFlow::MinimumCostFlow(int n) : BaseNetwork(n), pre(new int[n]), low(new int[n]),
                                              vis(new int[n]), clk(0) {
        memset(vis, 0, sizeof(int) * n);
    }

    MinimumCostFlow::~MinimumCostFlow() {
        delete[] pre;
        delete[] low;
        delete[] vis;
    }

    bool MinimumCostFlow::bfs(int S, int T) {
        vis[S] = ++clk, low[S] = INF, memset(dist, 0x3f, sizeof(int) * n), dist[S] = 0;
        std::queue<int> que;
        que.push(S);
        while (!que.empty()) {
            int u = que.front();
            que.pop();
            vis[u] = -1;
            for (int i = graph.head[u]; ~i; i = graph.edges[i].next) {
                int v = graph.edges[i].v, flow = graph.edges[i].flow, cost = graph.edges[i].cost;
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
        std::queue<int>().swap(que);
        return dist[T] < INF;
    }

    std::pair<ll, ll> MinimumCostFlow::run(int S, int T) {
        ll flow = 0, cost = 0;
        while (bfs(S, T)) {
            flow += low[T];
            cost += 1ll * low[T] * dist[T];
            for (int u = T; u != S; u = graph.edges[pre[u]].u) {
                graph.edges[pre[u]].flow -= low[T];
                graph.edges[pre[u] ^ 1].flow += low[T];
            }
        }
        return std::make_pair(flow, cost);
    }
}
