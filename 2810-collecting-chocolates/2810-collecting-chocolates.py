class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n=len(nums)
        ans = math.inf
        minCost=[math.inf]*n

        for i in range(n):
            for j in range(n):
                minCost[j]=min(minCost[j],nums[(j-i+n)%n])
            ans=min(ans,sum(minCost)+i*x)
        
        return ans