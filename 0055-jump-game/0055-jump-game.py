class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #nums[i] will be true if nums[j] is true and i-j<= jumpvalue 
        #must be solved throguh bottom up
        n = len(nums)
        last = n-1
        for i in range(n-2, -1, -1):
            if nums[i]+i >= last:
                last = i
        
        return last == 0