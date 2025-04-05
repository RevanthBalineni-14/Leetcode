class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def xor(arr):
            res = 0
            for i in arr:
                res = res^i
            return res

        def traverse(curr, n):
            if n==len(nums):
                res.append(xor(curr))
                return
            traverse(curr, n+1)
            traverse(curr + [nums[n]], n+1)
        
        traverse([], 0)
        return sum(res)