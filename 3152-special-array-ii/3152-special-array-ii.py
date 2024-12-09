from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefixarr = [0]*len(nums)
        for i in range(1, len(nums)):
            prefixarr[i] = prefixarr[i-1]
            if nums[i]%2 == nums[i-1]%2:
                prefixarr[i] += 1
        res = []
        
        for st, end in queries:
            if prefixarr[end]-prefixarr[st]>0:
                res.append(False)
            else:
                res.append(True)
        
        return res