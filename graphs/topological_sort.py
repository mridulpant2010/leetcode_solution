from collections import deque
class Solution:
    
    def adjacency_list(self,nodes,edges):
        graph={node:[] for node in nodes}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            self.in_degree[edge[1]]+=1
        return graph
    

    def topoSort(self, V,edges):
        # Code heref
        hash_set = set(range(V))
        self.in_degree = {node: 0 for node in hash_set}
        graph = self.adjacency_list(hash_set,edges)
        
        
        q= deque()
        for k,v in self.in_degree.items():
            if v == 0:
                q.append(k)
        
        res=[]
        while q:
            node = q.popleft()
            res.append(node)
            if len(graph[node])>0:
                for neighbor in graph[node]:
                    self.in_degree[neighbor]-=1
                    if self.in_degree[neighbor] == 0:
                        q.append(neighbor)
        
        return res

if __name__ == "__main__":
    sol = Solution()
    edges = [[1,2],[1,0]]
    res= sol.topoSort(3,edges)
    print(res)