class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0]*len(nums)
        pref[0] = nums[0]
        for i in range(1,len(nums)):
            pref[i] = pref[i-1]+nums[i]
        nums[0] = pref[len(nums)-1]-pref[0]-nums[0]*(len(nums)-1)
        for i in range(1,len(nums)):
            nums[i] = abs(nums[i]*(i)-pref[i-1])+pref[len(nums)-1]-pref[i]-nums[i]*(len(nums)-i-1)
        return nums