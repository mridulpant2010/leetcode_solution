from collections import defaultdict,deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def add_edge(self,v1,v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    def display(self):
        for vertex,neighbors in self.graph.items():
            print(f"{vertex}:{neighbors}")
    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            currentNode = queue.popleft()
            print(f"{currentNode}")
            for neighbors in self.graph[currentNode]:
                if neighbors not in visited:
                    queue.append(neighbors)
                    visited.add(neighbors)
    
    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, current_vertex, visited):
        if current_vertex not in visited:
            print(current_vertex, end=" ")
            visited.add(current_vertex)

            for neighbor in self.graph[current_vertex]:
                self._dfs(neighbor, visited)


if __name__ == "__main__":
    g = Graph()
    # g.add_vertex(1)
    # g.add_vertex(2)
    # g.add_vertex(3)
    # g.add_vertex(4)
    # Adding edges
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    # Displaying the graph
    g.display()
    g.bfs(1)
    g.dfs(1)
    
        