class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowfreq = [0]*m
        rowset = set()
        colfreq = [0]*n
        colset = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowfreq[i]+=1
                    colfreq[j]+=1
        for i in range(m):
            if rowfreq[i]>1:
                rowset.add(i)
        for j in range(n):
            if colfreq[j]>1:
                colset.add(j)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and ((i in rowset) or (j in colset)):
                    res += 1
        
        return res