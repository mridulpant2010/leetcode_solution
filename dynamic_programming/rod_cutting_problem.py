# https://www.geeksforgeeks.org/problems/rod-cutting0840/1

# the code for the rod cutting problem can be further optimised to work with a 1-d array.
class Solution:
    def cutRod(self, price):
        n = len(price)
        t = [[0 for _ in range(n+1)]for _ in range(n+1)]
        length = [i+1 for i in range(n)]
        #code here
        # for i in range(n+1):
        #     t[i][0]=0
            
        for i in range(n+1):
            for j in range(n+1):
                if length[i-1]<=j:
                    t[i][j]=max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][n]