import unittest

from flow_network import FlowNetwork


class MyTestCase(unittest.TestCase):
    def test_flow_network(self):
        flow_network = FlowNetwork(2)
        flow_network.add_edge(0, 1, 1)
        self.assertEqual(1, flow_network.run(0, 1))


if __name__ == '__main__':
    unittest.main()
