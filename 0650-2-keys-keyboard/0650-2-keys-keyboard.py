class Solution:
    def minSteps(self, n: int) -> int:
        if n==1: 
            return 0
        
        
        def findmin(curr, pl):
            if curr == n:
                return 0
            
            if curr>n:
                return 1000
            
            cp = 2+ findmin(curr*2, curr)
            p = 1+ findmin(curr+ pl, pl)
            
            return min(cp, p)
        
        return 1 + findmin(1,1)