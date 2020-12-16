from __future__ import absolute_import, print_function
import unittest

from .network import MaximumFlow, MinimumCostFlow


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

        maximum_flow.extract_graph()

        expected_flow = [1, 0, 0, 1, 1]

        self.assertEqual(expected_flow, [edge.flow for edge in maximum_flow.edges])

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

        flow, cost = minimum_cost_flow.run(0, 4)

        minimum_cost_flow.extract_graph()

        self.assertEqual(1, flow)
        self.assertEqual(4, cost)

        expect_flow = [1, 1, 1, 0, 0]

        self.assertEqual(expect_flow, [edge.flow for edge in minimum_cost_flow.edges])

    def test_flow_network(self):
        for backend in ['c', 'python']:
            self.maximum_flow_test(backend)
            self.minimum_cost_flow_test(backend)


if __name__ == '__main__':
    unittest.main()
