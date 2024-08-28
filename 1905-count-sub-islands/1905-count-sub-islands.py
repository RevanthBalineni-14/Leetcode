class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.m = len(grid2)
        self.n = len(grid2[0])
        self.grid1 = grid1
        self.grid2 = grid2
        res = 0
        self.iscurr = False
        def trav(self, i, j):
            if i>self.m-1 or i<0 or j>self.n-1 or j<0:
                return
            
            if self.grid2[i][j] == 0:
                return
            
            if self.grid1[i][j]!=self.grid2[i][j]:
                self.iscurr = False
                
           
            self.grid2[i][j] = 0
            trav(self, i-1, j)
            trav(self, i+1, j)
            trav(self, i, j-1)
            trav(self, i, j+1)
        
        for i in range(self.m):
            for j in range(self.n):
                if grid2[i][j]==1:
                    self.iscurr = True
                    trav(self, i, j)
                    if self.iscurr:
                        res+=1
        
        return res     