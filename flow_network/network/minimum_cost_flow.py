from __future__ import absolute_import, print_function
from flow_network.util import c_type_transfer, tuple_modifier, index_validator
from .network import NetWork
import ctypes
import typing


class MinimumCostFlow(NetWork):

    def __init__(self, n: int):
        super().__init__(n, 'minimum_cost_flow')
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
        index_validator(u, v, self._n)

        self.edges.append((u, v, flow, cost))
        self.edges.append((v, u, 0, -cost))

        c_u: ctypes.c_int = c_type_transfer(u)
        c_v: ctypes.c_int = c_type_transfer(v)
        c_flow: ctypes.c_int = c_type_transfer(flow)
        c_cost: ctypes.c_int = c_type_transfer(cost)
        self._clib.minimum_cost_flow_add_edge(self._obj, c_u, c_v, c_flow, c_cost)

    def run(self, s: int, t: int) -> (int, int):
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow, cost
        """
        c_result = (ctypes.c_int * 2)()
        self._run(s, t, c_result)
        flow, cost = int(c_result[0]), int(c_result[1])
        return flow, cost
