class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        suffix = [0]*n
        
        suffix[-1] = piles[-1]
        
        for i in range(n-2,-1,-1):
            suffix[i] = piles[i]+suffix[i+1]
        
        def findMax(i, M):
            if i>=n:
                return 0
            
            if (i, M) in dp:
                return dp[(i,M)]
            maxst = 0
            for X in range(1, 2*M+1):
                if i+X<= n:
                    maxst = max(maxst, suffix[i]-findMax(X+i, max(M,X)))
                
            dp[(i,M)] = maxst
            return maxst
        
        return findMax(0,1)