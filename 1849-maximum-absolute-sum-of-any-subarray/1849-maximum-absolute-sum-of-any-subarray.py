class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cmax, cmin = 0 , 0
        cpsum,cnsum = 0, 0
        for i in nums:
            cpsum += i
            if cpsum>cmax:
                cmax = cpsum
            if cpsum<0:
                cpsum = 0
            cnsum += i
            if cnsum<cmin:
                cmin = cnsum
            if cnsum>0:
                cnsum = 0

        return max(cmax, -cmin)