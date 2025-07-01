class Solution:
    # Function to find all possible paths
    def solve(self,maze,x,y,path,ans):
        if x<0 or y<0 or x>=self.n or y>=self.n or maze[x][y]!=1:
            return 
        
        if x==self.n-1 and y==self.n-1:
            ans.append("".join(path))
            return 
        
        maze[x][y]=0
        for k in range(4):
            ii = x + self.dx[k]
            jj = y + self.dy[k]
            path.append(self.path[k])
            self.solve(maze,ii,jj,path,ans)
            path.pop()
        maze[x][y]=1
    def ratInMaze(self, maze):
        # code here
        # self.dx = [-1,0,1,0]
        # self.dy = [0,1,0,-1]
        # self.path = ['D','R','U','L']
        self.dx = [1, 0, 0, -1]
        self.dy = [0, -1, 1, 0]
        self.path = ['D', 'L', 'R', 'U']
        self.n = len(maze)
        ans=[]
        if maze[0][0] == 1:
            self.solve(maze,0,0,[],ans)
        return ans

            