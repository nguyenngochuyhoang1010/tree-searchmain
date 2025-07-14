import heapq
from models.node import Node
from utils.grid import get_neighbors
from utils.path import reconstruct_path

def heuristic(pos, goals):
    return min(abs(pos[0] - gx) + abs(pos[1] - gy) for gx, gy in goals)

def search(start, goals, walls, grid_size):
    start_node = Node(start, heuristic=heuristic(start, goals))
    frontier = [start_node]
    heapq.heapify(frontier)
    visited = set()
    num_nodes = 0

    while frontier:
        node = heapq.heappop(frontier)
        num_nodes += 1

        if node.state in goals:
            return node.state, num_nodes, reconstruct_path(node)

        if node.state in visited:
            continue
        visited.add(node.state)

        for action, neighbor in get_neighbors(node.state, grid_size, walls):
            if neighbor not in visited:
                h = heuristic(neighbor, goals)
                heapq.heappush(frontier, Node(neighbor, node, action, heuristic=h))

    return None, num_nodes, []