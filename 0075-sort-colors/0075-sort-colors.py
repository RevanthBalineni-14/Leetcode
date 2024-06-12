class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        seeker  = 0
        two = len(nums)-1
        while seeker <= two :
            if nums[seeker] == 0:
                temp = nums[zero]
                nums[zero] = nums[seeker]
                nums[seeker] = temp
                zero += 1
                seeker +=1
            elif nums[seeker] == 1:
                seeker +=1
            else:
                temp = nums[seeker]
                nums[seeker]=nums[two]
                nums[two]=temp
                two -= 1
                
