from models.node import Node
from utils.grid import get_neighbors
from utils.path import reconstruct_path

def dls(node, goals, walls, grid_size, depth_limit, visited):
    """
    Depth-Limited Search (DLS).
    This is a recursive helper function that performs a depth-first search
    but stops exploring a path once it reaches the specified depth_limit.

    Returns:
        Node: The goal node if found within the depth limit, otherwise None.
    """
    # Base case 1: If the current node's state is a goal, we've found a solution.
    if node.state in goals:
        return node
    
    # Base case 2: If the depth limit is reached, stop exploring this path.
    if depth_limit <= 0:
        return None

    # Add the current node's state to the visited set for this DLS run.
    visited.add(node.state)

    # Explore neighbors recursively.
    for action, neighbor_state in get_neighbors(node.state, grid_size, walls):
        # Only explore neighbors that haven't been visited in this iteration.
        if neighbor_state not in visited:
            # Create a new node for the neighbor.
            neighbor_node = Node(neighbor_state, node, action)
            # Recursively call DLS for the neighbor with a decreased depth limit.
            result = dls(neighbor_node, goals, walls, grid_size, depth_limit - 1, visited)
            # If a solution was found in the recursive call, propagate it up.
            if result:
                return result
                
    # If no goal was found in any of the branches from this node, return None.
    return None

def search(start, goals, walls, grid_size):
    """
    Custom Search 1: Implemented as Iterative Deepening Search (IDS).
    
    """
    # Start the search at depth 0.
    depth = 0
    num_nodes = 0 # To count total nodes explored across all iterations.

    # This loop will run indefinitely, increasing the depth limit each time,
    # until a solution is found.
    while True:
        # For each new depth limit, we need a fresh set of visited nodes.
        # This is crucial because a node might be revisited on a deeper search.
        visited = set()
        
        # Create the initial node for the search.
        start_node = Node(start)
        
        # Perform a Depth-Limited Search (DLS) for the current depth.
        node = dls(start_node, goals, walls, grid_size, depth, visited)
        
        # Add the number of nodes visited in this iteration to the total count.
        num_nodes += len(visited)
        
        # If DLS found a solution (returned a node), we are done.
        if node:
            # Reconstruct the path from the goal node back to the start.
            path = reconstruct_path(node)
            return node.state, num_nodes, path
        
        # If no solution was found at the current depth, increase the depth limit
        # and start the next iteration.
        depth += 1
