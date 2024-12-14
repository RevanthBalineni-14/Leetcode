class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def traverse(j, xx, yy):
            if j>=n:
                return 0
            xx = min(xx, nums[j])
            yy = max(yy, nums[j])
            if abs(yy-xx)<=2:
                return 1+traverse(j+1, xx, yy)
            return 0
        res = 0
        for i in range(n):
            res += traverse(i, nums[i], nums[i])
        return res