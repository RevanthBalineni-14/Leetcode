class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def recurse(rem, crt):
            if not rem:
                res.append(crt)
                return
            
            n = len(rem)
            
            for i in range(n):
                if i<n-1 and rem[i]==rem[i+1]:
                    continue
                    
                recurse(rem[:i]+rem[i+1:], crt + [rem[i]])
                
        recurse(nums, [])
        return res