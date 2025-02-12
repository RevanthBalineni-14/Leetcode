from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mydic = defaultdict(list)
        sumnums = [0]*len(nums)
        for index, i in enumerate(nums):
            for j in str(i):
                sumnums[index] += int(j)
        
        for index, i in enumerate(sumnums):
            mydic[i].append(nums[index])
        
        res = -1
        for key in mydic:
            if len(mydic[key])>1:
                mydic[key].sort()
                res = max(res, mydic[key][-1]+mydic[key][-2])
        return res