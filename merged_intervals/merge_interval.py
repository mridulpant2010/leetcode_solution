class Pair:
    def __init__(self,x,y):
        self.start=x
        self.end=y
class Solution(object):
    def merge(self, arr):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        mergedInterval=[]
        arr.sort(key=lambda x: x[0])
        prev_el = Pair(arr[0][0],arr[0][1])
        for i in range(1,len(arr)):
            curr_el = Pair(arr[i][0],arr[i][1])
            if curr_el.start<=prev_el.end:
                prev_el.end=max(prev_el.end,curr_el.end)
                mergedInterval.append([prev_el.start,prev_el.end])
                prev_el.start=curr_el.start
                prev_el.end=curr_el.end
        mergedInterval.append([prev_el.start,prev_el.end])
        return mergedInterval
    

import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        he=[]
        for el in intervals:
            heapq.heappush(he,[el[0],el[1]])
        
        mergedInterval=[]
        while len(he)>0:
            first_element = heapq.heappop(he)
            if mergedInterval and mergedInterval[-1][1]>= first_element[0]:
                mergedInterval[-1][1] = max(mergedInterval[-1][1],first_element[1])
            else:
                mergedInterval.append(first_element)
        return mergedInterval