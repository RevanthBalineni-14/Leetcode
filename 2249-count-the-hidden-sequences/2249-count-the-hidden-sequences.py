class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        currSum = 0
        cmin, cmax = float('inf'), float('-inf')
        for i in differences:
            currSum += i
            cmin = min(cmin, currSum)
            cmax = max(cmax, currSum)
        res = 0
        for i in range(lower, upper+1):
            if (i+cmin)>=lower and (i+cmax)<=upper:
                res+=1
        return res