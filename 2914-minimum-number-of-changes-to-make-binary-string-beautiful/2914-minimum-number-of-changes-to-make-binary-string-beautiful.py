class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(len(s)//2):
            curra, currb = s[2*i], s[2*i+1]
            if curra != currb:
                res += 1
        
        return res