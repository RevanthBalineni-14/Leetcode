class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for i in nums:
            max_or = max_or | i
        
        def traverse(curr, ind):
            if ind == len(nums):
                if curr == max_or:
                    return 1
                else:
                    return 0 
            
            inc = traverse(curr | nums[ind], ind+1)
            exc = traverse(curr, ind+1)
            return (inc + exc)

        return traverse(0, 0)