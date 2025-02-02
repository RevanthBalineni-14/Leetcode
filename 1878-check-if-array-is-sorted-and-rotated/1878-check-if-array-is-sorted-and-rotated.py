class Solution:
    def check(self, nums: List[int]) -> bool:
        sortednums = sorted(nums)
        n = len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                if (nums[i+1:] + nums[:i+1]) == sortednums:
                    return True
                else:
                    return False
        
        return True