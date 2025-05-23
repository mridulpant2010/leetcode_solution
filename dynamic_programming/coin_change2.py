# https://leetcode.com/problems/coin-change-ii/
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        t = [[0 for _ in range(amount+1)]for _ in range(n+1)]
        for i in range(n+1):
            t[i][0]=1
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    t[i][j]= t[i][j-coins[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][amount]
        