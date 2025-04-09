class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        if nums[0]<k:
            return -1
        i = 0
        while i<len(nums):
            if nums[i]>k:
                break
            i+=1
        return len(nums)-i