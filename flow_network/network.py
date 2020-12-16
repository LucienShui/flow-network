from .core import CBaseNetwork, CMinimumCostFlow
from .pycore import PyMinimumCostFlow
from .edges import EdgeWithCost
from .core import CMaximumFlow
from .edges import Edge

import typing


class NetWork:

    def __init__(self, n: int, algorithm_name: str, c_backend, python_backend=None, backend: str = 'c'):
        super().__init__()

        self._algorithm_name = algorithm_name
        self._n: int = n

        if backend.lower() == 'python' and python_backend is not None:
            self._obj: CBaseNetwork = python_backend(n)
        else:
            self._obj: CBaseNetwork = c_backend(n)

        self.edges: typing.List[Edge] = ...

    def _run(self, s: int, t: int) -> [typing.Tuple, int]:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: tuple or int
        """
        result = self._obj.run(s, t)

        for i in range(0, len(self._obj.graph.edges), 2):
            self.edges[i >> 1].flow = self._obj.graph.edges[i ^ 1].flow

        return result

    def _add_edge(self, u: int, v: int, *args) -> None:

        if not 1 <= len(args) <= 2:
            raise AssertionError('length of args must >= 1 and <= 2')

        for arg in (u, v) + args:
            if not isinstance(arg, int):
                raise AssertionError(f'every arg should be type of int, got {type(arg)}')

        for node in ['u', 'v']:
            if eval(node) < 0:
                raise AssertionError(f'index of {node} is {eval(node)}, which should be greater or equal to 0')

            if eval(node) >= self._n:
                raise AssertionError(f'index of {node} is {eval(node)}, which should be less than n = {self._n}')

        self._obj.graph.add_edge(u, v, *args)

    def summary(self, line_length: int = 32, print_fn=print):
        vertex_cnt: int = self._n
        edge_cnt: int = len(self.edges)

        print_fn(f'''{'=' * line_length}
{' '.join([each.capitalize() for each in self._algorithm_name.split('_')])}
{'-' * line_length}
Number of vertices: {vertex_cnt}
Number of edges: {edge_cnt}
{"=" * line_length}''')

    def extract_graph(self, print_fn=print):
        print_fn('\n'.join(
            [
                'u -> v, flow / capacity' + ', cost' if isinstance(self.edges[0], EdgeWithCost) else ''
            ] + [
                str(edge) for edge in self.edges
            ]))


class MaximumFlow(NetWork):

    def __init__(self, n: int, backend: str = 'c'):
        super().__init__(n, 'flow_network', CMaximumFlow, None, backend)
        self.edges: typing.List[Edge] = []
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
        self.edges.append(Edge(u, v, flow))

    def run(self, s: int, t: int) -> int:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow
        """
        return self._run(s, t)


class MinimumCostFlow(NetWork):

    def __init__(self, n: int, backend: str = 'c'):
        super().__init__(n, 'minimum_cost_flow', CMinimumCostFlow, PyMinimumCostFlow, backend)
        self.edges: typing.List[EdgeWithCost] = []

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
        self.edges.append(EdgeWithCost(u, v, flow, cost))

    def run(self, s: int, t: int) -> (int, int):
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: flow, cost
        """
        flow, cost = self._run(s, t)
        return flow, cost
