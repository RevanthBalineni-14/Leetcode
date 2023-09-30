class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        iarr = [0]*len(nums)
        minval = nums[0]
        iarr[0] = nums[0]
        for i in range(len(nums)):
            if minval<nums[i]:
                iarr[i] = minval
            else:
                minval = nums[i]
                iarr[i] = minval

        stack = []

       
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > iarr[j]:
                while stack and stack[-1] <= iarr[j]:
                    stack.pop()
                if stack and stack[-1]<nums[j]:
                    return True
                stack.append(nums[j])        
        
        return False