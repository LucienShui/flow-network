from __future__ import absolute_import, print_function
from flow_network.core import CMinimumCostFlow
from flow_network.python_backend import PyMinimumCostFlow
from .network import NetWork
import typing


class MinimumCostFlow(NetWork):

    def __init__(self, n: int, backend: str = 'c'):
        super().__init__(n, 'minimum_cost_flow', CMinimumCostFlow, PyMinimumCostFlow, backend)
        self.edges: typing.List[typing.Tuple[int, int, int, int]] = []

    def add_edge(self, u: int, v: int, flow: int, cost: int) -> None:
        """
        add edge from u to v with flow and cost
        :param u: point's index
        :param v: point's index
        :param flow: edge capacity
        :param cost: cost for cutting an edge
        :return: None
        """
        self._add_edge(u, v, flow, cost)
        self.edges.append((u, v, flow, cost))
        self.edges.append((v, u, 0, -cost))

    def run(self, s: int, t: int) -> (int, int):
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow, cost
        """
        flow, cost = self._run(s, t)
        return flow, cost
