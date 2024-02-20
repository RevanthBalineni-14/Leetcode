class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mysum = (len(nums)*(len(nums)+1))//2
        for i in nums:
            mysum -= i
        return mysum