from collections import deque
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.dx=[-1,0,1,0]
        self.dy=[0,1,0,-1] ; ans=0
        self.m = len(grid)
        self.n = len(grid[0]) 

        q= deque()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]==2:
                    q.append((i,j))
        # run the multi-level bfs
        while len(q)>0:
            size = len(q) ; temp=0
            for _ in range(size):
                x,y=q.popleft()
                for i in range(4):
                    xx= x+self.dx[i]
                    yy= y+self.dy[i]
                    if xx>=0 and xx<self.m and yy>=0 and yy<self.n and grid[xx][yy]==1:
                        temp=1
                        grid[xx][yy]=2
                        q.append((xx,yy))
            ans+=temp
        for row in grid:
            if 1 in row:
                return -1

        return ans