class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return matrix[0][0]
        n = len(matrix)
        dp = [[0] * n for _ in range(n)] 
        dp = matrix.copy()
        
        for i in range(n-2,-1,-1):
            for j in range(n):
                minp = dp[i+1][j]
                if j-1 > -1:
                    minp = min(minp, dp[i+1][j-1])
                if j+1 < n:
                    minp = min(minp, dp[i+1][j+1])
                dp[i][j] += minp
        
        return min(dp[0])