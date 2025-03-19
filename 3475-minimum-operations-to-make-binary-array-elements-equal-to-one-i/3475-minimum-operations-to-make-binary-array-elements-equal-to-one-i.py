class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n-2):
            if nums[i]==0:
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                res+=1
        
        return res if (nums[n-2]==1 and nums[n-1]==1) else -1