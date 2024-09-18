class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
                
        def dfs(i, j, memo, triangle):
            if (i, j) in memo:
                return memo[(i,j)]
            
            if  i<len(triangle)-1:
                memo[(i,j)] = triangle[i][j] + min(dfs(i+1, j+1, memo, triangle), dfs(i+1, j, memo, triangle))
            else:
                memo[(i,j)] = triangle[i][j]
            
            return memo[(i,j)]
        
        return dfs(0, 0, memo, triangle)