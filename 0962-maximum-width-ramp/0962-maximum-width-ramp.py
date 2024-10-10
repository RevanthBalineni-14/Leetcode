class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        res = 0
        for i in range(len(nums)):
            if not st or nums[i]<nums[st[-1]]:
                st.append(i)
                
        for j in range(len(nums)-1, -1, -1):
            while st and nums[j]>=nums[st[-1]]:
                res = max(res, j-st[-1])
                st.pop()
                
        return res           