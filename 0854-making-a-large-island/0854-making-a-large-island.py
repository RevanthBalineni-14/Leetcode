class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.visited = [[False]*self.n for _ in range(self.n)]
        count = 2
        self.dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        for i in range(self.n):
            for j in range(self.n):
                if  not self.visited[i][j] and grid[i][j]==1:
                    self.bfs(grid, i, j, count)
                    count += 1

        sizemap = defaultdict(int)
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j]>1:
                    sizemap[grid[i][j]] += 1
        res = 0
        for i in sizemap:
            if (sizemap[i]+1)>res:
                res = sizemap[i]+1
        
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j]==0:
                    cres = 0
                    cset = set()
                    for direc in self.dirs:
                        dx = i + direc[0]
                        dy = j + direc[1]
                        if self.isValid(dx, dy):
                            cset.add(grid[dx][dy])

                    for k in cset:
                        cres += sizemap[k]
                    
                    cres+=1
                    if res<cres:
                        res = cres
        
        return min(res, self.n * self.n)

    
    def isValid(self, x, y):
        if 0<=x<self.n and 0<=y<self.n:
            return True
        
        return False

    def bfs(self, grid, x, y, count):
        if self.visited[x][y] == True or grid[x][y]==0:
            return

        grid[x][y] = count
        self.visited[x][y] = True

        for i in range(len(self.dirs)):
            dx = self.dirs[i][0] + x
            dy = self.dirs[i][1] + y
            if self.isValid(dx, dy):
                self.bfs(grid, dx, dy, count)
        
        return 
        