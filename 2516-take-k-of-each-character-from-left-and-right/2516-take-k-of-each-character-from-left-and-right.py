class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        totA, totB, totC = 0, 0, 0 
        
        for i in s:
            if i == 'a':
                totA += 1
            elif i== 'b':
                totB += 1
            elif i == 'c':
                totC += 1
        
        if totA<k or totB<k or totC<k:
            return -1
        
        l, r = 0,  0
        a, b, c = 0, 0, 0
        res = len(s)
        while r < len(s):
            
            a += 1 if s[r] == 'a' else 0
            b += 1 if s[r] == 'b' else 0
            c += 1 if s[r] == 'c' else 0
            
            while a > totA - k or b > totB-k or c  > totC-k:
                a -= 1 if s[l] == 'a' else 0
                b -= 1 if s[l] == 'b' else 0
                c -= 1 if s[l] == 'c' else 0
                l += 1
            
            res  = min(res, len(s) - (r-l+1))

            r += 1
        
        return res