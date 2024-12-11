class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        bounds = []
        for num in nums:
            bounds.append((num-k, 1))
            bounds.append((num+k+1, -1))
        
        bounds.sort()
        res = 1
        count = 0
        for bound, effect in bounds:
            count += effect
            res = max(res, count)
        return res