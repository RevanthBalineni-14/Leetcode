class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cov = 0
        pat = 0
        for num in nums:
            while num>cov+1:
                pat += 1
                cov = cov*2+1
                if cov>=n:
                    return pat
            
            cov += num
            if cov>=n:
                return pat
            
        while n>cov:
            pat+=1
            cov = cov*2 + 1
        
        return pat          