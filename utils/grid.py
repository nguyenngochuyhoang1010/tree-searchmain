def get_neighbors(state, grid_size, walls):
    x, y = state
    moves = [('UP', (x - 1, y)), ('LEFT', (x, y - 1)), 
             ('DOWN', (x + 1, y)), ('RIGHT', (x, y + 1))]

    in_bounds = lambda x, y: 0 <= x < grid_size[0] and 0 <= y < grid_size[1]

    valid = []
    for action, (nx, ny) in moves:
        if in_bounds(nx, ny) and not is_blocked(nx, ny, walls):
            valid.append((action, (nx, ny)))
    return valid

def is_blocked(x, y, walls):
    for wx, wy, w, h in walls:
        if wx <= x < wx + h and wy <= y < wy + w:
            return True
    return False
