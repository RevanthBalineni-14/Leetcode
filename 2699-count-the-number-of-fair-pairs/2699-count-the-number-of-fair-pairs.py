from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.countPairLessThan(nums, upper+1) - self.countPairLessThan(nums, lower)

    def countPairLessThan(self, nums, target):
        lo, hi = 0, len(nums)-1
        res = 0
        while(lo<hi):
            if (nums[hi]+nums[lo])<target:
                res += hi-lo
                lo += 1
            else:
                hi -= 1
        
        return res