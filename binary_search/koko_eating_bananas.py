#https://leetcode.com/problems/koko-eating-bananas/?envType=study-plan-v2&envId=leetcode-75

import math
class Solution:
    def get_cost(self,arr,k):
        sum_cost= 0 
        for i in range(len(arr)):
            sum_cost+= math.ceil(arr[i]/k)
        return sum_cost
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h: return -1
        max_k = max(piles)
        start=1
        calculated_cost=0
        end = max_k
        while start <= end:
            mid = (start + end)//2
            k = mid
            calculated_cost = self.get_cost(piles,k)
            if calculated_cost<=h:
                end = mid-1
            else:
                start=mid+1
        return start