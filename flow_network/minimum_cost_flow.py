from __future__ import absolute_import, print_function
from .util import c_type_transfer, tuple_modifier, index_validator
from .core import Clib
import ctypes
import typing


class MinimumCostFlow(Clib):
    def __init__(self, n: int):
        super().__init__()

        c_n: ctypes.c_int = c_type_transfer(n)

        self.__n = n

        self.__obj = self._clib.minimum_cost_flow_new.restype = ctypes.POINTER(ctypes.c_void_p)
        self.__obj = self._clib.minimum_cost_flow_new(c_n)

        self.edges: typing.List[typing.Tuple[int, int, int, int]] = []

    def __del__(self):
        self._clib.delete_minimum_cost_flow_ptr(self.__obj)

    def add_edge(self, u: int, v: int, flow: int, cost: int) -> None:
        """
        add edge from u to v with flow and cost
        :param u: point's index
        :param v: point's index
        :param flow: edge capacity
        :param cost: cost for cutting an edge
        :return: None
        """
        index_validator(u, v, self.__n)

        self.edges.append((u, v, flow, cost))
        self.edges.append((v, u, 0, -cost))

        c_u: ctypes.c_int = c_type_transfer(u)
        c_v: ctypes.c_int = c_type_transfer(v)
        c_flow: ctypes.c_int = c_type_transfer(flow)
        c_cost: ctypes.c_int = c_type_transfer(cost)
        self._clib.minimum_cost_flow_add_edge(self.__obj, c_u, c_v, c_flow, c_cost)

    def run(self, s: int, t: int) -> (int, int):
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow, cost
        """
        c_s: ctypes.c_int = c_type_transfer(s)
        c_t: ctypes.c_int = c_type_transfer(t)
        c_result = (ctypes.c_int * 2)()

        c_edge_flows = (ctypes.c_int * len(self.edges))()

        self._clib.minimum_cost_flow_run(self.__obj, c_s, c_t, c_result, c_edge_flows)
        flow, cost = int(c_result[0]), int(c_result[1])

        for idx, each in enumerate(c_edge_flows):
            self.edges[idx] = tuple_modifier(self.edges[idx], 2, int(each))

        return flow, cost
