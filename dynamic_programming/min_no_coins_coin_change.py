#https://leetcode.com/problems/coin-change/description/
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        t=[[0 for _ in range(amount+1)]for _ in range(n+1)]
        INT_MAX=sys.maxsize
        for j in range(amount+1):
            t[0][j]=INT_MAX-1
        
        if n>0:
            for j in range(1,amount+1):
                if j%coins[0]==0:
                    t[1][j]=j//coins[0]
                else:
                    t[1][j]=INT_MAX-1
        for i in range(2,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    t[i][j]=min(t[i][j-coins[i-1]]+1,t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        return -1 if t[n][amount]==INT_MAX-1 else t[n][amount]