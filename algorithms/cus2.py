import heapq
from models.node import Node
from utils.grid import get_neighbors
from utils.path import reconstruct_path

def heuristic(pos, goals):
    """
    Calculates the Manhattan distance to the nearest goal.
    """
    if not goals:
        return float('inf')
    return min(abs(pos[0] - gx) + abs(pos[1] - gy) for gx, gy in goals)

def search(start, goals, walls, grid_size):
    """
    Custom Search 2: Implemented as Weighted A*.
    Informed search that uses f(n) = g(n) + W * h(n), where W > 1.
    This tends to find solutions faster but is NOT guaranteed to find the shortest path
    if the base heuristic h(n) is admissible and W > 1, because W*h(n) can become inadmissible.
    """
    heuristic_weight = 2.0 # The weight W for the heuristic

    start_node = Node(start, cost=0, heuristic=heuristic_weight * heuristic(start, goals))
    
    frontier = []
    entry_count = 0
    heapq.heappush(frontier, (start_node.total_cost(), entry_count, start_node))
    entry_count +=1

    # explored_costs stores the minimum g_cost found so far to reach a state
    explored_costs = {start_node.state: 0}
    num_nodes_generated = 0

    while frontier:
        _, _, current_node = heapq.heappop(frontier)
        num_nodes_generated += 1

        if current_node.state in goals:
            return current_node.state, num_nodes_generated, reconstruct_path(current_node)

        if current_node.cost > explored_costs.get(current_node.state, float('inf')):
            continue

        for action, neighbor_state in get_neighbors(current_node.state, grid_size, walls):
            g_cost_to_neighbor = current_node.cost + 1 

            if g_cost_to_neighbor >= explored_costs.get(neighbor_state, float('inf')):
                continue
            
            explored_costs[neighbor_state] = g_cost_to_neighbor
            h_cost_neighbor = heuristic_weight * heuristic(neighbor_state, goals)
            neighbor_node = Node(state=neighbor_state,
                                 parent=current_node,
                                 action=action,
                                 cost=g_cost_to_neighbor,
                                 heuristic=h_cost_neighbor)
            heapq.heappush(frontier, (neighbor_node.total_cost(), entry_count, neighbor_node))
            entry_count += 1
            
    return None, num_nodes_generated, []
