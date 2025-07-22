class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r,csum, msum = 0, 0, 0, nums[0]
        prevocc = {}
        while r<len(nums):
            if nums[r] not in prevocc or prevocc[nums[r]] < l:
                csum += nums[r]
                msum = max(csum, msum)
            else:
                while l<=prevocc[nums[r]]:
                    csum -= nums[l]
                    l += 1
                csum += nums[r]    
            prevocc[nums[r]] = r
            r += 1
        return msum