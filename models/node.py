class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state  # (x, y)
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic

    def __lt__(self, other):
        return self.total_cost() < other.total_cost()