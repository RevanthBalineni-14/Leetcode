class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dp = [10001]*n
        dp[n-1] = 0

        for i in range(n-2, -1 ,-1):
            dp[i] = min(dp[i : nums[i]+i+1]) + 1
        
        return dp[0]