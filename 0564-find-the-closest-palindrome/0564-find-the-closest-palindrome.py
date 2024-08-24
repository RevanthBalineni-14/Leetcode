class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        cd = set()
        
        if n=='1':
            return '0'
        
        pref = n[:(l+1)//2]
        
        pref = int(pref)
        
        for i in [-1, 0, 1]:
            newp = str(pref+i)
            
            if l%2==1:
                newc = newp + str(newp[:-1][::-1])
            else:
                newc = newp + str(newp[::-1])
                
            cd.add(newc)
            
        cd.add(str(10**(l-1) - 1))
        cd.add(str(10**l + 1))
        
        cd.discard(n)
        
        closest_palindrome = min(cd, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest_palindrome       