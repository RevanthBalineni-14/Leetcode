class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix = [0]*(len(nums)+1)
        postfix = [0]*len(nums)

        for i in range(1, len(nums)+1):
            prefix[i] = max(prefix[i-1], nums[i-1])
        
        for i in range(len(nums)-2, -1,-1):
            postfix[i] = max(postfix[i+1], nums[i+1])
        res = 0
        for i in range(len(nums)):
            res = max(res, (prefix[i]-nums[i])*postfix[i])
        return res