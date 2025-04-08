class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freqMap = defaultdict(int)
        def checkMap():
            for key in freqMap:
                if freqMap[key]>1:
                    return False
            
            return True
        for num in nums:
            freqMap[num] += 1
        res = 0
        while not checkMap():
            for i in range(min(3, len(nums))):
                freqMap[nums[i]] -= 1
            nums = nums[3:]
            res += 1
        return res