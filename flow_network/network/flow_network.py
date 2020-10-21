from __future__ import absolute_import, print_function
from flow_network.util import c_type_transfer, tuple_modifier, index_validator
from .network import NetWork
import ctypes
import typing


class FlowNetwork(NetWork):

    def __init__(self, n: int):
        super().__init__(n, 'flow_network')
        self.edges: typing.List[typing.Tuple[int, int, int]] = []

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

        c_u: ctypes.c_int = c_type_transfer(u)
        c_v: ctypes.c_int = c_type_transfer(v)
        c_flow: ctypes.c_int = c_type_transfer(flow)
        self._clib.flow_network_add_edge(self._obj, c_u, c_v, c_flow)

    def run(self, s: int, t: int) -> int:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow, cost
        """
        c_result = (ctypes.c_int * 1)()
        self._run(s, t, c_result)
        result = int(c_result[0])
        return result
