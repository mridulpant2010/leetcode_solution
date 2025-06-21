from typing import List
import heapq
import math
from collections import deque
class Solution:
    
    def adjacency_graph(self,graph,edges):
        for edge in edges:
            graph[edge[0]].update({edge[1] : edge[2]}) 
        return graph
        
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        start_node=1
        end_node = n
        prev = {i+1:None for i in range(n)}
        distance = {i+1: math.inf   for i in range(n)}
        distance[start_node]=0
        graph  = self.adjacency_graph({i+1:{} for i in range(n)}, edges)
        print(graph)
        q = []
        res=[]
        heapq.heappush(q,(0,start_node))
        while q:
            c_dist , c_node = heapq.heappop(q)
            for nbr, dist in graph[c_node].items():
                new_dist = c_dist + dist
                if distance[nbr]>new_dist:
                    distance[nbr] = new_dist
                    prev[nbr] = c_node
                    heapq.heappush(q,(new_dist,nbr))        
        if distance[end_node] == math.inf:
            return [-1]
        res.append(nbr)
        last_node= prev[nbr]
        while last_node:
            res.append(last_node)
            if prev[last_node] is None:
                break
            else:
                last_node = prev[last_node]
        ans = deque(res[::-1])
        ans.appendleft(new_dist)
        return ans
        
        

if __name__ == "__main__":
    sol = Solution()
    edges = [[1,4,4],[2,5,6],[3,6,1],[4,5,5],[1,2,2]]
    res = sol.shortestPath(5,6,edges)
    print(res)
    