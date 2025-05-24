class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerop, twop = 0, len(nums)-1
        pointer = 0
        while pointer<=twop:
            if nums[pointer] == 0:
                nums[zerop], nums[pointer] = nums[pointer], nums[zerop]
                zerop += 1
                pointer += 1
            elif nums[pointer] == 1:
                pointer += 1
            else:
                nums[pointer], nums[twop] = nums[twop], nums[pointer]
                twop -= 1
        