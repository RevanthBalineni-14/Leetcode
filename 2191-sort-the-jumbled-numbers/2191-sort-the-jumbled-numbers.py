class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            num  = list(str(num))
            
            for i in range(len(num)):
                num[i] = str(mapping[int(num[i])])
            
            return int(''.join(num))
        
        mydic = {}
        for i in range(len(nums)):
            mydic[nums[i]] = convert(nums[i])
        
        nums = sorted(nums, key= lambda x: mydic[x])
        return nums