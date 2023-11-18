class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cs = 0
        res = 0
        nums.sort()
        if len(nums) == 1:
            return 1
        lval = 0
        rval = 0
        while rval < len(nums):
            cs  += nums[rval]
            while cs + k < nums[rval]*(rval-lval+1):
                cs = cs - nums[lval]
                lval += 1
            
            res = max(res, rval-lval+1)
            rval += 1
        
        return res