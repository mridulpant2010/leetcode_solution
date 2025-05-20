# https://leetcode.com/problems/target-sum/description/
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        subset_sum = (target+ sum(nums))//2

        return self.countSubsetSum(nums,subset_sum)
    
    def countSubsetSum(self,nums,s):
        n =len(nums)
        t = [[0 for j in range(s+1)]for i in range(n+1)]

        for i in range(n+1):
            for j in range(s+1):
                if i==0:
                    t[i][j]=0
                if j==0:
                    t[i][j]=1
        
        for i in range(1,n+1):
            for j in range(1,s+1):
                if nums[i-1]<=j:
                    t[i][j]=t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][s]
    
if __name__=="__main__":
    sol = Solution()
    nums = [1,1,1,1,1]; target = 3
    ans=sol.findTargetSumWays(nums,target)
    print(ans)
    