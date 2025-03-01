class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            if nums[i]!= 0 and nums[i]==nums[i+1]:
                nums[i+1] = 0 
                res.append(2*nums[i])
            elif nums[i] != 0:
                res.append(nums[i])

        if nums[-1] != 0:
            res.append(nums[-1])  

        diff = len(nums) - len(res)
        for i in range(diff):
            res.append(0)
        return res