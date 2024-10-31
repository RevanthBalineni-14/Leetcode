class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        m = len(robot)
        n = len(factory)
        
        dp = [0] + [float('inf')]*m
        for f, l in factory:
            for _ in range(l):
                for i, r in reversed(list(enumerate(robot))):
                    dp[i+1] = min(dp[i] + abs(r-f), dp[i+1] )
        
        return dp[-1]