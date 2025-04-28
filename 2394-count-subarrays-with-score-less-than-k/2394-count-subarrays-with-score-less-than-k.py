class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, 0
        currSum = 0
        for right in range(len(nums)):
            currSum += nums[right]
            if (currSum * (right-left+1))<k:
                res += right-left+1
            else:
                while left<len(nums) and (currSum * (right-left+1))>=k:
                    currSum -= nums[left]
                    left += 1
                res += right-left+1
        return res