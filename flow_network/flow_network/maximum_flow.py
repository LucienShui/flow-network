from __future__ import absolute_import, print_function
from flow_network.util import index_validator
from flow_network.core import CMaximumFlow
from .network import NetWork
import typing


class FlowNetwork(NetWork):

    def __init__(self, n: int):
        super().__init__(n, 'flow_network')
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
        index_validator(u, v, self._n)

        self.edges.append((u, v, flow))
        self.edges.append((v, u, 0))

        self._obj.graph.add_edge(u, v, flow)

    def run(self, s: int, t: int) -> int:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow
        """
        return self._run(s, t)
