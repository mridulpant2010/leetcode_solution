from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}
        for entry in prerequisites:
            graph[entry[1]].append(entry[0])
            indegree[entry[0]]+=1
        q=deque()
        for k,v in indegree.items():
            if v==0:
                q.append(k)
        
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        
        for k,v in indegree.items():
            if v!=0:
                return False
        return True