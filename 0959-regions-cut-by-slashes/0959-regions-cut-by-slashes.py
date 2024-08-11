class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.n = len(grid)
        res = 0
        self.cgrid = [[0 for i in range(self.n*3)] for j in range(self.n*3)]
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == "/":
                    self.cgrid[i*3+0][j*3+2] = -1
                    self.cgrid[i*3+1][j*3+1] = -1
                    self.cgrid[i*3+2][j*3+0] = -1
                elif grid[i][j] == "\\":
                    self.cgrid[i*3+0][j*3+0] = -1
                    self.cgrid[i*3+1][j*3+1] = -1
                    self.cgrid[i*3+2][j*3+2] = -1
        
        
        def fill(self, i, j):
            if i<0 or j<0 or i>=self.n*3 or j>=self.n*3 or self.cgrid[i][j]!=0:
                return
            self.cgrid[i][j] = -1
            
            fill(self, i+1, j)
            fill(self, i-1, j)
            fill(self, i, j+1)
            fill(self, i, j-1)
            
        for i in range(self.n*3):
            for j in range(self.n*3):
                if self.cgrid[i][j]==0:
                    res+=1
                    fill(self, i, j)
                   
        return res