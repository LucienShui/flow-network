from __future__ import absolute_import, print_function
from flow_network.core import CMaximumFlow
from .network import NetWork
import typing


class MaximumFlow(NetWork):

    def __init__(self, n: int, backend: str = 'c'):
        super().__init__(n, 'flow_network', CMaximumFlow, None, backend)
        self.edges: typing.List[typing.Tuple[int, int, int]] = []
        self._obj: CMaximumFlow = CMaximumFlow(n)

    def add_edge(self, u: int, v: int, flow: int) -> None:
        """
        add edge from u to v with flow and cost
        :param u: point's index
        :param v: point's index
        :param flow: edge capacity
        :return: None
        """
        self._add_edge(u, v, flow)
        self.edges.append((u, v, flow))
        self.edges.append((v, u, 0))

    def run(self, s: int, t: int) -> int:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow
        """
        return self._run(s, t)
