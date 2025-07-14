from collections import deque
from models.node import Node
from utils.grid import get_neighbors
from utils.path import reconstruct_path

def search(start, goals, walls, grid_size):
    stack = deque([Node(start)])
    visited = set()
    num_nodes = 0

    while stack:
        node = stack.pop()
        num_nodes += 1

        if node.state in goals:
            return node.state, num_nodes, reconstruct_path(node)

        if node.state in visited:
            continue
        visited.add(node.state)

        for action, neighbor in reversed(get_neighbors(node.state, grid_size, walls)):
            if neighbor not in visited:
                stack.append(Node(neighbor, node, action))
    return None, num_nodes, []
