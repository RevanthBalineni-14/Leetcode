class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        csum = sum(rolls)
        m = len(rolls)
        reqsum  = (m+n)*mean - csum
        
        if reqsum<n or reqsum>n*6:
            return []
        
        base = reqsum//n
        rem = reqsum%n
        res = [base]*n
        for i in range(rem):
            res[i] +=1
        
        return res       