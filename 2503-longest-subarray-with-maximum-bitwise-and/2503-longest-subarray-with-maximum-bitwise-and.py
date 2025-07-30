class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cmax = max(nums)
        res = 1
        def traverse(nums, i, maxv):
            end = i
            while end<len(nums) and nums[end] == maxv:
                end+=1
            return end
        i=0

        while i<(len(nums)):
            if nums[i]==cmax:
                end = traverse(nums, i, cmax)
                res = max(end-i, res)
                i = end
            i+=1
        return res