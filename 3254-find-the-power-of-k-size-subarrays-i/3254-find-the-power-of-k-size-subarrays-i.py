class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prearr = [0]*n
        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                prearr[i] = prearr[i-1]
            else:
                prearr[i] = i
        res = []
        for i in range(k - 1, n):
            if prearr[i] <= i - k + 1:
                res.append(nums[i])
            else:
                res.append(-1)
        return res
