class Edge(object):
    def __init__(self, u: int, v: int, capacity: int, flow: int = 0):
        self.u: int = u
        self.v: int = v
        self.capacity: int = capacity
        self.flow: int = flow


class EdgeWithCost(Edge):
    def __init__(self, u: int, v: int, capacity: int, cost: int, flow: int = 0):
        super().__init__(u, v, capacity, flow)
        self.cost: int = cost
