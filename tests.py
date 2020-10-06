import unittest

from flow_network import FlowNetwork, MinimumCostFlow


class FlowNetworkTestCase(unittest.TestCase):

    def test_flow_network(self):
        flow_network = FlowNetwork(5)

        # u, v, flow
        edges = [
            (0, 1, 1),
            (1, 2, 1),
            (2, 4, 2),
            (1, 3, 2),
            (3, 4, 1)
        ]

        for u, v, flow in edges:
            flow_network.add_edge(u, v, flow)

        self.assertEqual(1, flow_network.run(0, 4))

    def test_minimum_cost_flow(self):
        minimum_cost_flow = MinimumCostFlow(5)

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

        flow, cost = minimum_cost_flow.run(0, 4)
        self.assertEqual(1, flow)
        self.assertEqual(4, cost)


if __name__ == '__main__':
    unittest.main()
