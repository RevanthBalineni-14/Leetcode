class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = [num-int(str(num)[::-1]) for num in nums]
        res = 0
        for i in Counter(nums).values():
            res += (i*(i-1))//2
        
        return res%(10**9+7)