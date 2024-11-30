class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        bits = [0]*32
        
        left = 0
        right= 0
        
        res = len(nums)+1
        
        while left<=right and right<len(nums):
            temp = 0
            
            for i in range(32):
                if nums[right] & 1<<i:
                    bits[i] += 1
                if bits[i]>0:
                    temp |= 1<<i
            
            while temp>=k and left<=right:
                res = min(res, right-left+1)
                temp = 0
                for i in range(32):
                    if nums[left] & 1<<i:
                        bits[i] -= 1
                    if bits[i]>0:
                        temp |= 1<<i
                
                left += 1
                
            right += 1
                
        return -1 if res==(len(nums)+1) else res
    