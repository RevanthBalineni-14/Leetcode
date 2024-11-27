class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mydic = defaultdict(list)
        dp = [0]*n
        for i in range(n):
            dp[n-1-i] = i
        print(dp)
        res = []
        for q in range(len(queries)):
            dp[queries[q][0]] = min(dp[queries[q][0]], dp[queries[q][1]]+1)
            mydic[queries[q][0]].append(queries[q][1])
            
            for i in range(queries[q][0]-1, -1, -1):
                if len(mydic[i])==0 and i+1<=queries[q][0]:
                    dp[i] = min(dp[i], 1 + dp[i+1])
                else:
                    if i+1<=queries[q][0]:
                        dp[i] = min(dp[i], 1 + dp[i+1])
                    for j in mydic[i]:
                        dp[i] = min(dp[i], 1+dp[j])
            res.append(dp[0])
            print(dp)
        return res