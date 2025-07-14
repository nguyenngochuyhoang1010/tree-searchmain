def parse_problem(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    # Grid dimensions
    grid_line = lines[0].strip('[]')
    rows, cols = map(int, grid_line.split(','))

    # Initial position
    start = tuple(map(int, lines[1].strip('()').split(',')))

    # Goal positions
    goal_line = lines[2].split('|')
    
    goals = [tuple(map(int, g.strip().strip('()').split(','))) for g in goal_line]

    # Walls
    walls = [tuple(map(int, l.strip('()').split(','))) for l in lines[3:]]

    return (rows, cols), start, goals, walls
