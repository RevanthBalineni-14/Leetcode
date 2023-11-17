class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end  = len(nums)-1
        maxs = float('-inf')
        while start < end:
            maxs=max(maxs, nums[start]+nums[end])
            start += 1
            end -= 1
        
        return maxs