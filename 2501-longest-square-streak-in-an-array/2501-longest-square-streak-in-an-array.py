class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        numset = set(nums)
        currind = len(nums)-1
        curr = nums[currind]
        currlen = 1
        while currind>0:
            if curr in numset and (curr**0.5) in numset:
                currlen += 1
                res = max(res, currlen)
                numset.remove(curr)
                curr = (curr**0.5)
                
            else:
                currind -= 1
                while currind>-1 and nums[currind] not in numset:
                    currind -= 1
                    
                if currind<0:
                    break
                curr = nums[currind]
                currlen = 1
                
        return res