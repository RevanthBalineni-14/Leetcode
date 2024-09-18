class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m  = len(word1)
        n = len(word2)
        
        def distcal(word1, word2, memo, m, n):
            if m==0:
                return n
            if n==0:
                return m
            
            if memo[m][n] != -1:
                return memo[m][n]
            
            if word1[m-1]==word2[n-1]:
                memo[m][n] = distcal(word1, word2, memo, m-1, n-1)
            else:
                memo[m][n] = 1 + min(distcal(word1, word2, memo, m-1, n-1), distcal(word1, word2, memo, m-1, n), distcal(word1, word2, memo, m, n-1))
            
            return memo[m][n]
        
        memo = [[-1]*(n+1) for _ in range(m+1)]
        
        return distcal(word1, word2, memo, m, n)