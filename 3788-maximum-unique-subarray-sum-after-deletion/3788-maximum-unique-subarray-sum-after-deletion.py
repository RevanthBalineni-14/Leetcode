class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res, cmin = 0, float('-inf')
        flag = False
        cset = set()
        for i in nums:
            if i>-1 and i not in cset:
                cset.add(i)
                flag = True
                res += i
            elif i<0:
                cmin = max(i, cmin)
        if flag:
            return res
        else:
            return cmin