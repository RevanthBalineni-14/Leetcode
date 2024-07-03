class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res=float("inf")
        for a,b in zip(nums[:4], nums[-4:]):
            res = min(b-a, res)
            
        return res