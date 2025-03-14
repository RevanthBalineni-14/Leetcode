class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        res = 0
        while l<=r:
            mid = (l+r)//2
            npiles = sum(pilesize//mid for pilesize in candies)
            if npiles >= k:
                l = mid+1
                res = mid
            else:
                r = mid-1
        
        return res