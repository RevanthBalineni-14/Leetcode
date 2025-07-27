class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev, res = None, 0
        for i in range(1, len(nums)-1):
            if nums[i]-nums[i-1]>0:
                prev = True
            elif nums[i]-nums[i-1]<0:
                prev = False
            
            if (nums[i+1]-nums[i])>0 and prev==False:
                res += 1
            elif (nums[i+1]-nums[i])<0 and prev:
                res += 1
            
            print(i, res)
        return res