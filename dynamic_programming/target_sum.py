# https://leetcode.com/problems/target-sum/description/
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum =(target+ sum(nums))
        if total_sum %2!=0 or sum(nums)<abs(target):
            return 0
        subset_sum = total_sum//2
        return self.countSubsetSum(nums,subset_sum)
    
    def countSubsetSum(self,nums,s):
        n =len(nums)
        t = [[0 for _ in range(s+1)]for _ in range(n+1)]

        for i in range(n+1):
            t[i][0]=1
        
        for i in range(1,n+1):
            for j in range(s+1):
                if nums[i-1]<=j:
                    t[i][j]=t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][s]
        
if __name__=="__main__":
    sol = Solution()
    #nums = [1,1,1,1,1]; target = 3
    nums=[0]; target=0
    ans=sol.findTargetSumWays(nums,target)
    print(ans)
    