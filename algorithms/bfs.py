from collections import deque
from models.node import Node
from utils.grid import get_neighbors
from utils.path import reconstruct_path

def search(start, goals, walls, grid_size):
    queue = deque([Node(start)])
    visited = set()
    num_nodes = 0

    while queue:
        node = queue.popleft()
        num_nodes += 1

        if node.state in goals:
            return node.state, num_nodes, reconstruct_path(node)

        if node.state in visited:
            continue
        visited.add(node.state)

        for action, neighbor in get_neighbors(node.state, grid_size, walls):
            if neighbor not in visited:
                queue.append(Node(neighbor, node, action))
    return None, num_nodes, []
