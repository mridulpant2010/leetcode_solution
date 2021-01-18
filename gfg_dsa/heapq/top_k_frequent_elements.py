import heapq
from collections import defaultdict


def topKFrequent(nums,K):
    d = defaultdict(int)
    for el in nums:
        d[el]+=1
    heap=[]
    heapq.heapify(heap)
    for k,v in d.items():
        heapq.heappush(heap,(v,k))
        if len(heap)>K:
            heapq.heappop(heap)
    print([each[1] for each in heap])

topKFrequent([1,1,1,2,2,3],2)