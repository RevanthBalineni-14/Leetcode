class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        res = sys.maxsize
        nums = sorted(set(nums))
        for i, ele in enumerate(nums):
            maxv=ele+n-1
            idx = bisect_right(nums, maxv)
            res = min(res,n-(idx-i))
        return res

        