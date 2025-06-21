from collections import defaultdict, deque

def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge.split('-')
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfs(start, graph):
    visited = set()
    queue = deque([(start, 0)])
    farthest_node = start
    max_dist = 0

    while queue:
        node, dist = queue.popleft()
        visited.add(node)
        if dist > max_dist:
            max_dist = dist
            farthest_node = node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
    return farthest_node, max_dist

def farthest_nodes_bfs(edges):
    graph = build_graph(edges)
    start = next(iter(graph))  # Pick any node
    far_node, diameter = bfs(start, graph)
    #_, diameter = bfs(far_node, graph)
    return diameter

# Example usage
edges = ["b-a","c-e","b-c","d-c"]
#["b-e","b-c","c-d","a-b","e-f"]
#["a-b", "b-c", "b-d"]
print(farthest_nodes_bfs(edges))  # Output: 2