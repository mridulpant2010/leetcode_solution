'''
leetcode url: https://leetcode.com/problems/sort-characters-by-frequency/
'''

from collections import defaultdict
import heapq

def frequencySort(s):
    heap=[]
    heapq.heapify(heap)
    d= defaultdict(int)
    for el in s :
        d[el] +=1
    print(d)
    for k,v in d.items():
        heapq.heappush(heap,(-1*v,k))
    while len(heap)>0:
        top= heapq.heappop(heap)
        c=top[0]*-1
        while c:
            print(top[1],end='',sep='')
            c-=1
        
    
frequencySort('Aabb')