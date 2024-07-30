class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        bpre, apos = [0]*n, [0]*n
        
        if s[0]=='b':
            bpre[0] = 1
        
        apos[0] = s.count('a')
        
        for i in range(1,n):
            if s[i]=='b':
                bpre[i] = bpre[i-1] + 1
            else:
                bpre[i] = bpre[i-1]
                
            if s[i-1]=='a':
                apos[i] = apos[i-1] - 1 
            else:
                apos[i] = apos[i-1]
            
        
        res = n 
        for i in range(n):
            res = min(res, bpre[i]+apos[i]-1)
        
        return res