class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ctarr = [0]*50001
        for i in nums:
            ctarr[i] += 1
        
        res = 0
        op = 0
        for i in range(50000,0,-1):
            if ctarr[i]>0:
                res += op
                op += ctarr[i]
        
        return res