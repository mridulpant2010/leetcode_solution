# https://leetcode.com/problems/find-k-closest-elements/
import heapq,math
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        he = []
        for el in arr:
            cal = abs(el-x)
            heapq.heappush(he,(-cal,el))
            while len(he)>k:
                heapq.heappop(he)
        return he
    
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 4 
    x = 3
    s = Solution()
    res= s.findClosestElements(arr,k,x)
    print(res)
