class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        j = 0
        k= n-1
        res = []
        for i in range(n):
            if abs(nums[j])>abs(nums[k]):
                res.append(nums[j]**2)
                j += 1
            else:
                res.append(nums[k]**2)
                k -= 1
        
        return res[::-1]