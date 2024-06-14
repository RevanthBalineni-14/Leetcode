class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        mininc = 0
        for i in range(0,len(nums)-1):
            if nums[i+1]<= nums[i]:
                mininc += (nums[i]-nums[i+1])+1
                nums[i+1] += (nums[i]-nums[i+1])+1
        
        return mininc