def reconstruct_path(node):
    path = []
    while node.parent:
        path.append(node.action)
        node = node.parent
    return path[::-1]