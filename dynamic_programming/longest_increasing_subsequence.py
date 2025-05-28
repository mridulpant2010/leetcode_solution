class Solution:

    def LCS(self,a,b):
        m=len(a)
        n=len(b)
        t = [[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1]==b[j-1]:
                    t[i][j] = t[i-1][j-1]+1
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        return t[m][n]


    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_nums=sorted(set(nums))
        lis_count= self.LCS(nums,sorted_nums)
        return lis_count
