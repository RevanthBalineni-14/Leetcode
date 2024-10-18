class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_b = 0
        for i in nums:
            max_b = max_b | i
            
        
        def backtrack( ind, c_or):
            if ind == len(nums):
                if c_or == max_b:
                    return 1
                else:
                    return 0
            
            inc = backtrack(ind+1, c_or | nums[ind])
            exc = backtrack(ind+1, c_or)
            
            return inc+exc
        
        return backtrack(0, 0)