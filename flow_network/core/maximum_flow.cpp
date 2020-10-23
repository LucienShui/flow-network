#include <queue>
#include "maximum_flow.h"

namespace flow_network {

    MaximumFlow::MaximumFlow(int n) : BaseNetwork(n), cur(new int[n]) {}

    MaximumFlow::~MaximumFlow() {
        delete[] cur;
    }

    bool MaximumFlow::bfs(int S, int T) {
        memset(dist, 0xff, sizeof(int) * n);
        dist[S] = 0;
        std::queue<int> que;
        que.push(S);
        while (!que.empty()) {
            int u = que.front();
            que.pop();
            for (int i = graph.head[u]; ~i; i = graph.edges[i].next) {
                int v = graph.edges[i].v, flow = graph.edges[i].flow;
                if (dist[v] == -1 && flow > 0) {
                    dist[v] = dist[u] + 1;
                    if (v == T) return true;
                    que.push(v);
                }
            }
        }
        return false;
    }

    int MaximumFlow::dfs(int u, int T, int low) {
        if (u == T) return low;
        for (int &i = cur[u]; ~i; i = graph.edges[i].next) {
            int v = graph.edges[i].v, flow = graph.edges[i].flow;
            if (dist[v] == dist[u] + 1 && flow > 0) {
                int min = dfs(v, T, flow < low ? flow : low);
                if (min > 0) {
                    graph.edges[i].flow -= min;
                    graph.edges[i ^ 1].flow += min;
                    return min;
                }
            }
        }
        return 0;
    }

    int MaximumFlow::run(int S, int T) {
        int ans = 0, tmp;
        while (bfs(S, T)) {
            memcpy(cur, graph.head, sizeof(int) * n);
            while (tmp = dfs(S, T), tmp > 0) ans += tmp;
        }
        return ans;
    }
}