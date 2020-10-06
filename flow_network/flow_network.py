from __future__ import absolute_import, print_function
from .util import c_type_transfer
import ctypes
import os


class FlowNetwork:

    def __init__(self, n: int):
        c_n: ctypes.c_int = c_type_transfer(n)

        lib_path = os.path.join(os.getcwd(), 'flow_network/lib/flow-network.so')

        if not os.path.exists(lib_path):
            raise AssertionError(f'{lib_path} not found')

        self.__flow_network_clib = ctypes.CDLL(lib_path)
        # self.__obj = self.__flow_network_clib.hello_world.restype = ctypes.c_void_p
        # self.__obj = self.__flow_network_clib.hello_world()
        self.__obj = self.__flow_network_clib.flow_network_new.restype = ctypes.Structure
        self.__obj = self.__flow_network_clib.flow_network_new(c_n)

    def add_edge(self, u: int, v: int, flow: int):
        c_u: ctypes.c_int = c_type_transfer(u)
        c_v: ctypes.c_int = c_type_transfer(v)
        c_flow: ctypes.c_int = c_type_transfer(flow)
        self.__flow_network_clib.flow_network_add_edge(self.__obj, c_u, c_v, c_flow)

    def run(self, s: int, t: int) -> int:
        c_s: ctypes.c_int = c_type_transfer(s)
        c_t: ctypes.c_int = c_type_transfer(t)
        c_result = (ctypes.c_int * 1)()
        self.__flow_network_clib.flow_network_run(self.__obj, c_s, c_t, c_result)
        result = int(c_result[0])
        return result
