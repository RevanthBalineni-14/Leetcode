class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = 1 - nums[0]%2
        for i in range(len(nums)):
            curr = nums[i]%2
            if curr!=prev:
                prev = curr
            else:
                return False
        
        return True