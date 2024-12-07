class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def checker(penality):
            currop = 0
            for i in nums:
                if i>penality:
                    currop += (i-1)//penality
            if currop>maxOperations:
                return False
            else:
                return True
        
        left, right = 1, max(nums)
        
        while left<right:
            mid = left + (right-left)//2
            if checker(mid):
                right = mid
            else:
                left = mid+1
        
        return left