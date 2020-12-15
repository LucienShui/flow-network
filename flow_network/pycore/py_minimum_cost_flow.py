from __future__ import absolute_import, print_function

import typing
from queue import Queue

INF = 0x3f3f3f3f


class Edge:

    def __init__(self, _next: int, u: int, v: int, flow: int, cost: int):
        self.next_idx = _next
        self.u = u
        self.v = v
        self.flow = flow
        self.cost = cost


class Graph:

    def __init__(self, n: int):
        self.n = n
        self.cnt = 0
        self.head: typing.List[int] = [-1] * n
        self.edges: typing.List[Edge] = []

    def __add_edge(self, u: int, v: int, flow: int, cost: int = 0):
        self.edges.append(Edge(self.head[u], u, v, flow, cost))
        self.head[u] = self.cnt
        self.cnt += 1

    def add_edge(self, u: int, v: int, flow: int, cost: int = 0):
        self.__add_edge(u, v, flow, cost)
        self.__add_edge(v, u, 0, -cost)


class PyMinimumCostFlow:

    def __init__(self, n: int):
        self.n: int = n
        self.graph: Graph = Graph(n)

        self.clk: int = 0

        self.dist: typing.List[int] = ...
        self.pre: typing.List[int] = [0] * n
        self.low: typing.List[int] = [0] * n
        self.vis: typing.List[int] = [0] * n

        self._algorithm_name: str = 'minimum_cost_flow'

    def __bfs(self, s: int, t: int) -> bool:
        self.clk += 1
        self.vis[s] = self.clk
        self.low[s] = INF
        self.dist = [INF] * self.n
        self.dist[s] = 0

        que: Queue = Queue()
        que.put(s)

        while not que.empty():
            u = que.get()
            self.vis[u] = -1

            i = self.graph.head[u]
            while i != -1:
                v = self.graph.edges[i].v
                flow = self.graph.edges[i].flow
                cost = self.graph.edges[i].cost

                if self.dist[v] > self.dist[u] + cost and flow > 0:
                    self.dist[v] = self.dist[u] + cost
                    self.pre[v] = i
                    self.low[v] = min(self.low[u], flow)

                    if self.vis[v] != self.clk:
                        que.put(v)
                        self.vis[v] = self.clk

                i = self.graph.edges[i].next_idx

        return self.dist[t] < INF

    def run(self, s: int, t: int) -> (int, int):
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow, cost
        """

        flow = cost = 0

        while self.__bfs(s, t):
            flow += self.low[t]
            cost += self.low[t] * self.dist[t]
            u = t
            while u != s:
                self.graph.edges[self.pre[u]].flow -= self.low[t]
                self.graph.edges[self.pre[u] ^ 1].flow += self.low[t]

                u = self.graph.edges[self.pre[u]].u

        return flow, cost
