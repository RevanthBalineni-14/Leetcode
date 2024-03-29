class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        maxp = ((n)*(n-1))//2
        if k>maxp:
            return 0
        if k==maxp or k==0:
            return 1
        
        mod = 10**9+7
        
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][0]=1
        
        dp[2][1]=1
        
        for i in range(3, n+1):
            maxp = min(k, ((i)*(i-1))//2)
            for j in range(1, maxp+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if j>=i:
                    dp[i][j] -= dp[i-1][j - i]
                dp[i][j] = (dp[i][j] + mod) % mod
        return dp[n][k]