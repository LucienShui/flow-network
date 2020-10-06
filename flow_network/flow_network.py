from __future__ import absolute_import, print_function
from .util import c_type_transfer, tuple_modifier
import ctypes
import typing
import os


class FlowNetwork:

    def __init__(self, n: int):
        c_n: ctypes.c_int = c_type_transfer(n)

        lib_path = os.path.join(os.getcwd(), 'flow_network/lib/flow-network.so')

        if not os.path.exists(lib_path):
            raise AssertionError(f'{lib_path} not found')

        self.__n = n

        self.__flow_network_clib = ctypes.cdll.LoadLibrary(lib_path)
        self.__obj = self.__flow_network_clib.flow_network_new.restype = ctypes.POINTER(ctypes.c_void_p)
        self.__obj = self.__flow_network_clib.flow_network_new(c_n)

        self.edges: typing.List[typing.Tuple[int, int, int]] = []

    def __del__(self):
        self.__flow_network_clib.delete_ptr(self.__obj)

    def add_edge(self, u: int, v: int, flow: int) -> None:
        """
        add edge from u to v with flow and cost
        :param u: point's index
        :param v: point's index
        :param flow: edge capacity
        :return: None
        """
        if u >= self.__n:
            raise AssertionError(f'index of u is {u}, which should be less than n = {self.__n}')

        if v >= self.__n:
            raise AssertionError(f'index of v is {v}, which should be less than n = {self.__n}')

        self.edges.append((u, v, flow))
        self.edges.append((v, u, 0))

        c_u: ctypes.c_int = c_type_transfer(u)
        c_v: ctypes.c_int = c_type_transfer(v)
        c_flow: ctypes.c_int = c_type_transfer(flow)
        self.__flow_network_clib.flow_network_add_edge(self.__obj, c_u, c_v, c_flow)

    def run(self, s: int, t: int) -> int:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow, cost
        """
        c_s: ctypes.c_int = c_type_transfer(s)
        c_t: ctypes.c_int = c_type_transfer(t)
        c_result = (ctypes.c_int * 1)()

        c_edge_flows = (ctypes.c_int * len(self.edges))()

        self.__flow_network_clib.flow_network_run(self.__obj, c_s, c_t, c_result, c_edge_flows)
        result = int(c_result[0])

        for idx, each in enumerate(c_edge_flows):
            self.edges[idx] = tuple_modifier(self.edges[idx], 2, int(each))

        return result


class MinimumCostFlow:
    def __init__(self, n: int):
        c_n: ctypes.c_int = c_type_transfer(n)

        lib_path = os.path.join(os.getcwd(), 'flow_network/lib/flow-network.so')

        if not os.path.exists(lib_path):
            raise AssertionError(f'{lib_path} not found')

        self.__n = n

        self.__flow_network_clib = ctypes.cdll.LoadLibrary(lib_path)
        self.__obj = self.__flow_network_clib.minimum_cost_flow_new.restype = ctypes.POINTER(ctypes.c_void_p)
        self.__obj = self.__flow_network_clib.minimum_cost_flow_new(c_n)

        self.edges: typing.List[typing.Tuple[int, int, int, int]] = []

    def __del__(self):
        self.__flow_network_clib.delete_ptr(self.__obj)

    def add_edge(self, u: int, v: int, flow: int, cost: int) -> None:
        """
        add edge from u to v with flow and cost
        :param u: point's index
        :param v: point's index
        :param flow: edge capacity
        :param cost: cost for cutting an edge
        :return: None
        """
        if u >= self.__n:
            raise AssertionError(f'index of u is {u}, which should be less than n = {self.__n}')

        if v >= self.__n:
            raise AssertionError(f'index of v is {v}, which should be less than n = {self.__n}')

        self.edges.append((u, v, flow, cost))
        self.edges.append((v, u, 0, -cost))

        c_u: ctypes.c_int = c_type_transfer(u)
        c_v: ctypes.c_int = c_type_transfer(v)
        c_flow: ctypes.c_int = c_type_transfer(flow)
        c_cost: ctypes.c_int = c_type_transfer(cost)
        self.__flow_network_clib.minimum_cost_flow_add_edge(self.__obj, c_u, c_v, c_flow, c_cost)

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

        self.__flow_network_clib.minimum_cost_flow_run(self.__obj, c_s, c_t, c_result, c_edge_flows)
        flow, cost = int(c_result[0]), int(c_result[1])

        for idx, each in enumerate(c_edge_flows):
            self.edges[idx] = tuple_modifier(self.edges[idx], 2, int(each))

        return flow, cost
