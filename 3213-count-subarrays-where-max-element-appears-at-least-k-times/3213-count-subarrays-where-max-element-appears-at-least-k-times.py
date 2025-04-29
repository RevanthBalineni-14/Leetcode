class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        nmax = max(nums)
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == nmax:
                count += 1
            while count == k:
                res += len(nums)-right 
                if nums[left] == nmax:
                    count -= 1
                left += 1
                
        return res