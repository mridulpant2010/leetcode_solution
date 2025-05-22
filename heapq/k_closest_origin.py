import heapq,math
from collections import defaultdict
def close_point(a,b):
    ans= math.sqrt(a*a+ b*b)
    #d[(a,b)]=ans
    return ans

def kClosest(points,K):
    heap=[]
    d =defaultdict(tuple)
    heapq.heapify(heap)
    for each_element in points:
        a,b = each_element
        ans = close_point(a,b)
        d[(a,b)]=ans
    for k,v in d.items():
        heapq.heappush(heap,(-1*v,k))
        if len(heap)>K:
            heapq.heappop(heap)
    print(heap)
    return [list(each[1]) for each in heap]
        
            
print(kClosest([[1,3],[-2,2]],1))
        
        

