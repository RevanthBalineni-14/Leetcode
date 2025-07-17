class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        res = 2
        for i in range(0,k):
            dp = [0]*k

            for j in range(len(nums)):
                mod = nums[j]%k
                pos = (i-mod+k)%k
                dp[mod] = dp[pos]+1

            for val in dp:
                res = max(val, res)
        return res