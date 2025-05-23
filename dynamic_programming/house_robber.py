# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        self.dp = [0 for _ in range(n+1)]
        self.dp[0]=0
        self.dp[1]=nums[0]
        for i in range(2,n+1):
            self.dp[i]=max(self.dp[i-1],nums[i-1]+self.dp[i-2])  
        return self.dp[n]  