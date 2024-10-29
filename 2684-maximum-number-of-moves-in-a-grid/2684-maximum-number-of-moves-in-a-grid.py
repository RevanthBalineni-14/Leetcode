class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [-1, 1], [1,1]]
        memo = {}
        
        def dfs(row, col):
            if col == n-1:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            mm = 0
            
            curr = grid[row][col]
            
            for dr, dc in dirs:
                nrow, ncol = row + dr, col + dc
                if nrow>-1 and nrow<m and ncol>-1 and ncol<n and grid[nrow][ncol]>curr:
                     mm = max(mm, 1+dfs(nrow, ncol))
            
            memo[(row, col)] = mm
            return mm
        
        res = 0
        for i in range(m):
            res = max(res, dfs(i, 0))
        
        return res                    