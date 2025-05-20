class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        netoper = [0]*(len(nums))
        for q in queries:
            netoper[q[0]] -= 1
            if (q[1]+1)<len(nums):
                netoper[q[1]+1] += 1
        runningtotal = 0
        for i in range(len(nums)):
            runningtotal += netoper[i]
            nums[i] += runningtotal
            if nums[i]>0:
                return False
        return True