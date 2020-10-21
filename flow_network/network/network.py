from __future__ import absolute_import, print_function

import typing

from flow_network.util import c_type_transfer, tuple_modifier
from flow_network.core import Clib
import ctypes


class NetWork(Clib):

    def __init__(self, n: int, algorithm_name: str):
        super().__init__()

        self._n: int = n
        self._algorithm_name: str = algorithm_name

        exec(f'self._clib.{self._algorithm_name}_new.restype = ctypes.POINTER(ctypes.c_void_p)')

        self._init_function = eval(f'self._clib.{self._algorithm_name}_new')
        self._run_function = eval(f'self._clib.{self._algorithm_name}_run')
        self._delete_function = eval(f'self._clib.delete_{self._algorithm_name}_ptr')

        c_n: ctypes.c_int = c_type_transfer(self._n)
        self._obj = self._init_function(c_n)

        self.edges: typing.List[tuple] = ...

    def __del__(self) -> None:
        self._delete_function(self._obj)

    def _run(self, s: int, t: int, c_result: ctypes.Array) -> None:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :param c_result: c type result
        :return: None
        """
        c_s: ctypes.c_int = c_type_transfer(s)
        c_t: ctypes.c_int = c_type_transfer(t)

        c_edge_flows = (ctypes.c_int * len(self.edges))()

        self._run_function(self._obj, c_s, c_t, c_result, c_edge_flows)

        for idx, each in enumerate(c_edge_flows):
            self.edges[idx] = tuple_modifier(self.edges[idx], 2, int(each))

    def summary(self, line_length: int = 32, print_fn=print):
        vertex_cnt: int = self._n
        edge_cnt: int = len(self.edges)

        print_fn(f'''{"=" * line_length}
{' '.join([each.capitalize() for each in self._algorithm_name.split('_')])}
{"-" * line_length}
Number of vertices: {vertex_cnt}
Number of edges: {edge_cnt}
{"=" * line_length}''')
