class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            points, skip = questions[i]
            newi = skip+i+1
            if newi >= n:
                dp[i] = max(dp[i+1], points)
            else:
                dp[i] = max(points+dp[newi], dp[i+1])
        
        return dp[0]