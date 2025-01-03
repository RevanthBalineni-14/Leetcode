class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefarr = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefarr[0] = nums[0]
            else:
                prefarr[i] = nums[i]+prefarr[i-1]
        
        res = 0
        for i in range(len(nums)):
            if prefarr[i]>=(prefarr[-1]-prefarr[i]) and i<(len(nums)-1):
                res += 1
        
        return res