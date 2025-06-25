from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graphs = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}

        for entry in prerequisites:
            graphs[entry[1]].append(entry[0])
            indegree[entry[0]]+=1
        q=deque()
        for k,v in indegree.items():
            if v == 0:
                q.append(k)
        res=[]
        while q:
            curr =  q.popleft()
            res.append(curr)
            for neighbor in graphs[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        for k,v in indegree.items():
            if v != 0:
                return []
        return res