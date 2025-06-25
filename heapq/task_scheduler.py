from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        d = defaultdict(int)
        maxgaps=0
        he=[]
        for t in tasks:
            d[t]+=1
        for k,v in d.items():
            maxgaps = max(maxgaps,v)
            heapq.heappush(he,(-v,k))
        maxgaps=(maxgaps-1)
        idle_slots = maxgaps * (n+1)
        while len(he)>0:
            v , k = heapq.heappop(he)
            v= -1*v
            idle_slots -= min(maxgaps,v)
        if idle_slots<0:
            idle_slots=0
        ans = len(tasks)+ idle_slots
        return ans

s = Solution()
tasks = ["X","X","Y","Y"] 
n = 2
res=s.leastInterval(tasks,n)
print(res)