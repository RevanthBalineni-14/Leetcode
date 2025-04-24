class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniqueNums = set(nums)

        def checkHasUnique(left, right, uniqueNums):
            currNums = set(nums[left : right+1])
            if currNums == uniqueNums:
                return True
            else:
                return False
        
        left, right = 0, 0
        res = 0
        while left<=right and right<len(nums):
            if checkHasUnique(left, right, uniqueNums):
                res += len(nums)-right
                left += 1
                if left > right:
                    right+=1
            else:
                right += 1
        return res