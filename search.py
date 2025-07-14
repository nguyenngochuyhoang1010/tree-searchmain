import sys

from algorithms import dfs, bfs, gbfs, astar, cus1, cus2
from utils.parser import parse_problem

def main():
    if len(sys.argv) < 3:
        print("Usage: python search.py <filename> <method>")
        print("Example: python search.py testcases/test1.txt dfs")
        sys.exit(1)

    filename, method = sys.argv[1], sys.argv[2].lower()
    
    try:
        grid_size, start, goals, walls = parse_problem(filename)
    except FileNotFoundError:
        print(f"Error: Problem file '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error parsing problem file '{filename}': {e}")
        sys.exit(1)

    search_functions = {
        'dfs': dfs.search,
        'bfs': bfs.search,
        'gbfs': gbfs.search,
        'as': astar.search,  # 'as' for A* as per assignment PDF
        'cus1': cus1.search,
        'cus2': cus2.search,
    }

    search_fn = search_functions.get(method)
    if not search_fn:
        print(f"Unsupported search method: {method}")
        print(f"Available methods: {', '.join(search_functions.keys())}")
        sys.exit(1)

    # Execute the selected search function
    # The search functions are expected to return: (goal_state, num_nodes_expanded, path_list)
    # or (None, num_nodes_expanded, []) if no goal is found.
    result = search_fn(start, goals, walls, grid_size)
    
    # Check if result is None or not in the expected format (robustness)
    if result is None or not isinstance(result, tuple) or len(result) != 3:
        print(f"Error: Search function for method '{method}' did not return expected output.")
        # Optionally, print what was returned for debugging: print(f"Returned: {result}")
        # Defaulting num_nodes for printing if result is malformed
        num_nodes_for_print = 'N/A'
        if result is not None and isinstance(result, tuple) and len(result) > 1:
            num_nodes_for_print = result[1] if isinstance(result[1], int) else 'N/A'

        print(f"\n{filename} {method}")
        print(f"No goal is reachable; {num_nodes_for_print}") # Fallback if result format is wrong
        sys.exit(1)

    goal_node_state, num_nodes, path = result

    # Output results
    print(f"\n{filename} {method}") # Added a newline for better readability, matching example
    if goal_node_state:
        # Ensure goal_node_state is printed as a tuple string if it's a tuple
        goal_str = str(goal_node_state) if isinstance(goal_node_state, tuple) else goal_node_state
        print(f"{goal_str} {num_nodes}")
        print(str(path)) # Print path as a list string, e.g., ['UP', 'RIGHT']
    else:
        print(f"No goal is reachable; {num_nodes}")

if __name__ == "__main__":
    main()