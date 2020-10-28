import typing

from flow_network.util import tuple_modifier
from flow_network.core import CBaseNetwork


class NetWork:

    def __init__(self, n: int, algorithm_name: str, c_backend, python_backend=None, backend: str = 'c'):
        super().__init__()

        self._algorithm_name = algorithm_name
        self._n: int = n

        if backend.lower() == 'python' and python_backend is not None:
            self._obj: CBaseNetwork = python_backend(n)
        else:
            self._obj: CBaseNetwork = c_backend(n)

        self.edges: typing.List[tuple] = ...

    def _run(self, s: int, t: int) -> [typing.Tuple, int]:
        """
        inference
        :param s: source point's index
        :param t: target point's index
        :return: tuple or int
        """
        result = self._obj.run(s, t)

        for idx, edge in enumerate(self._obj.graph.edges):
            self.edges[idx] = tuple_modifier(self.edges[idx], 2, int(edge.flow))

        return result

    def _add_edge(self, u: int, v: int, *args) -> None:

        if len(args) > 2:
            raise AssertionError('')

        for node in ['u', 'v']:
            if eval(node) < 0:
                raise AssertionError(f'index of {node} is {eval(node)}, which should be greater or equal to 0')

            if eval(node) >= self._n:
                raise AssertionError(f'index of {node} is {eval(node)}, which should be less than n = {self._n}')

        self._obj.graph.add_edge(u, v, *args)

    def summary(self, line_length: int = 32, print_fn=print):
        vertex_cnt: int = self._n
        edge_cnt: int = len(self.edges)

        print_fn(f'''{"=" * line_length}
{' '.join([each.capitalize() for each in self._algorithm_name.split('_')])}
{"-" * line_length}
Number of vertices: {vertex_cnt}
Number of edges: {edge_cnt}
{"=" * line_length}''')

    def extract_graph(self, filepath) -> None:
        edge_cnt: int = len(self.edges)

        content = f'{self._n} {edge_cnt >> 1}\n'

        end_line: str = '\n'

        for i in range(0, edge_cnt, 2):
            each = self.edges[i]
            length = len(each)
            for j in range(length):
                content += f'{each[j]}{end_line if j == length - 1 else " "}'

        with open(filepath, 'w') as file:
            file.write(content)
