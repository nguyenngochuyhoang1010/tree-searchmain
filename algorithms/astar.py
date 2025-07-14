# algorithms/astar.py
import heapq
from models.node import Node
from utils.grid import get_neighbors
from utils.path import reconstruct_path

def heuristic(pos, goals):
    """
    Calculates the Manhattan distance to the nearest goal.
    This is an admissible heuristic (never overestimates the true cost).
    """
    if not goals:
        return float('inf')
    return min(abs(pos[0] - gx) + abs(pos[1] - gy) for gx, gy in goals)

def search(start, goals, walls, grid_size):
    """
    A* search algorithm.
    Finds the shortest path from start to one of the goals.
    Uses f(n) = g(n) + h(n), where:
    - g(n) is the cost from the start node to node n.
    - h(n) is the heuristic estimate of the cost from n to the goal.
    """
    # Initialize the start node
    # cost (g-value) is 0, heuristic (h-value) is calculated
    start_node = Node(start, parent=None, action=None, cost=0, heuristic=heuristic(start, goals))

    # Frontier is a priority queue, ordered by f_cost (total_cost)
    # We store (f_cost, unique_id, node) to handle tie-breaking if f_costs are equal.
    # A simple counter can serve as a unique_id for tie-breaking.
    frontier = []
    entry_count = 0 # Counter for tie-breaking
    heapq.heappush(frontier, (start_node.total_cost(), entry_count, start_node))
    entry_count += 1

    # explored_costs stores the minimum g_cost found so far to reach a state
    # {(x,y): g_cost}
    explored_costs = {start_node.state: 0}
    
    num_nodes_generated = 0 # Counter for nodes added to frontier (or considered)

    while frontier:
        f_cost, _, current_node = heapq.heappop(frontier)
        num_nodes_generated +=1 # Conventionally, a node is "expanded" or "visited" when popped

        # Goal check
        if current_node.state in goals:
            return current_node.state, num_nodes_generated, reconstruct_path(current_node)

        # If we've already found a shorter path to current_node.state, skip
        # This check is particularly important if nodes can be re-added to the frontier
        # (e.g. if not checking explored_costs before pushing).
        # With the check before pushing, this might seem redundant but is a good safeguard.
        if current_node.cost > explored_costs.get(current_node.state, float('inf')):
            continue

        # Expand neighbors
        for action, neighbor_state in get_neighbors(current_node.state, grid_size, walls):
            g_cost_to_neighbor = current_node.cost + 1 # Assuming cost of each step is 1

            # If this path to neighbor_state is worse than one already found, skip
            if g_cost_to_neighbor >= explored_costs.get(neighbor_state, float('inf')):
                continue

            # Update explored_costs and add to frontier
            explored_costs[neighbor_state] = g_cost_to_neighbor
            h_cost_neighbor = heuristic(neighbor_state, goals)
            neighbor_node = Node(state=neighbor_state,
                                 parent=current_node,
                                 action=action,
                                 cost=g_cost_to_neighbor,
                                 heuristic=h_cost_neighbor)
            heapq.heappush(frontier, (neighbor_node.total_cost(), entry_count, neighbor_node))
            entry_count += 1
            
    return None, num_nodes_generated, [] # No path found

