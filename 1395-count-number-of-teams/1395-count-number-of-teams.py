class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for i in range(n):
            ll, lg, rl, rg = 0, 0, 0, 0
            for j in range(i):
                if rating[j]<rating[i]:
                    ll +=1
                if rating[j]>rating[i]:
                    lg+=1
            for k in range(i+1, n):
                if rating[i]<rating[k]:
                    rg +=1
                if rating[i]>rating[k]:
                    rl+=1
            
            res += ll*rg + lg*rl
        
        return res