from __future__ import absolute_import, print_function
import unittest

from flow_network import MaximumFlow, MinimumCostFlow


class FlowNetworkTestCase(unittest.TestCase):

    def maximum_flow_test(self, backend: str = 'c'):
        maximum_flow = MaximumFlow(5, backend)

        # u, v, flow
        edges = [
            (0, 1, 1),
            (1, 2, 1),
            (2, 4, 2),
            (1, 3, 2),
            (3, 4, 1)
        ]

        for u, v, flow in edges:
            maximum_flow.add_edge(u, v, flow)

        maximum_flow.summary()

        self.assertEqual(1, maximum_flow.run(0, 4))

        self.assertEqual(0, maximum_flow.edges[0][2])
        self.assertEqual(1, maximum_flow.edges[1][2])

    def minimum_cost_flow_test(self, backend: str = 'c'):
        minimum_cost_flow = MinimumCostFlow(5, backend)

        # u, v, flow, cost
        edges = [
            (0, 1, 1, 1),
            (1, 2, 1, 1),
            (2, 4, 2, 2),
            (1, 3, 2, 2),
            (3, 4, 1, 4)
        ]

        for u, v, flow, cost in edges:
            minimum_cost_flow.add_edge(u, v, flow, cost)

        minimum_cost_flow.summary()
        minimum_cost_flow.extract_graph('graph.txt')

        flow, cost = minimum_cost_flow.run(0, 4)

        self.assertEqual(1, flow)
        self.assertEqual(4, cost)

        self.assertEqual(0, minimum_cost_flow.edges[0][2])
        self.assertEqual(1, minimum_cost_flow.edges[1][2])

    def test_flow_network(self):
        for backend in ['c', 'python']:
            self.maximum_flow_test(backend)
            self.minimum_cost_flow_test(backend)

    def test_tuple_modifier(self):
        from flow_network.util import tuple_modifier
        buf = (1, 2, 3)
        result = tuple_modifier(buf, 1, 4)
        self.assertEqual((1, 4, 3), result)


if __name__ == '__main__':
    unittest.main()
