class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tmod = sum(nums)%p
        if tmod == 0:
            return 0
        
        mydic = {0:-1}
        pref = 0
        minl = len(nums)
        
        for i in range(len(nums)):
            pref = (pref + nums[i])%p
            
            req = (pref - tmod + p)%p
            if req in mydic:
                minl = min(minl, i - mydic[req])
            mydic[pref] = i
            
        return minl if minl<len(nums) else -1