class Solution:
    def setZeroes(self, a) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        frow=False
        m = len(a)
        n = len(a[0])
        if not a or not a[0]:
            return 
        for i in range(m):
            for j in range(n):
                if a[i][j]==0:
                    if i==0:
                        frow=True
                    else:
                        a[0][j]=0
                        a[i][0]=0
        
        # traverse the column
        for j in range(1,n):
            if a[0][j]==0:
                for i in range(1,m):
                    a[i][j]=0
                    
        
        #traverse the row
        for i in range(1,m):
            if a[i][0]==0:
                for j in range(1,n):
                    a[i][j]=0
        
        if frow:
            for i in range(m):
                a[i][0]=0
            for j in range(n):
                a[0][j]=0

if __name__=="__main__":
    s = Solution()
    matrix= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    print(matrix)