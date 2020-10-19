#include "flow-network.h"

#include <cstring>
#include <map>
#include <queue>

namespace flow_network {

    FlowNetwork::FlowNetwork(int n) : dist(new int[n]), cur(new int[n]), n(n), graph(n) {}

    bool FlowNetwork::bfs(int S, int T) {
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

    int FlowNetwork::dfs(int u, int T, int low) {
        if (u == T) return low;
        for (int &i = cur[u]; ~i; i = graph.edge[i].next) {
            int v = graph.edge[i].v, flow = graph.edge[i].flow;
            if (dist[v] == dist[u] + 1 && flow > 0) {
                int min = dfs(v, T, flow < low ? flow : low);
                if (min > 0) {
                    graph.edge[i].flow -= min;
                    graph.edge[i ^ 1].flow += min;
                    return min;
                }
            }
        }
        return 0;
    }

    int FlowNetwork::run(int S, int T) {
        int ans = 0, tmp;
        while (bfs(S, T)) {
            memcpy(cur, graph.head, sizeof(int) * n);
            while (tmp = dfs(S, T), tmp > 0) ans += tmp;
        }
        return ans;
    }

    MinimumCostFlow::MinimumCostFlow(int n, int m) : dist(new int[n]), pre(new int[n]), low(new int[n]),
                                                     vis(new int[n]), que(new int[n]), clk(0), n(n), m(m),
                                                     size_of_array(sizeof(int) * n), graph(n, m) {}

    bool MinimumCostFlow::bfs(int S, int T) {
        vis[S] = ++clk, low[S] = INF, memset(dist, 0x3f, size_of_array), dist[S] = 0;
        int head = 0, tail = 0;
        que[tail++] = S;
        while (head != tail) {
            int u = que[head++];

            if (head >= n) {
                head -= n;
            }

            vis[u] = -1;
            for (int i = graph.head[u]; ~i; i = graph.edge[i].next) {
                int v = graph.edge[i].v, flow = graph.edge[i].flow, cost = graph.edge[i].cost;
                if (dist[v] > dist[u] + cost && flow > 0) {
                    dist[v] = dist[u] + cost;
                    pre[v] = i;
                    low[v] = std::min(low[u], flow);
                    if (vis[v] != clk) {
                        que[tail++] = v;

                        if (tail >= n) {
                            tail -= n;
                        }

                        vis[v] = clk;
                    }
                }
            }
        }
        return dist[T] < INF;
    }

    std::pair<int, int> MinimumCostFlow::run(int S, int T) {
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
}
