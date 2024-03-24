class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
        return 0