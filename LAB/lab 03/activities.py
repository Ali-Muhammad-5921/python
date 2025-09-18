# Activity 1-b: BFS from A to F
from collections import deque

def bfs_path(graph, start, goal):
    queue = deque([[start]])  # store paths
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

path = bfs_path(graph, 'A', 'F')
print("BFS Path from A to F:", path)


