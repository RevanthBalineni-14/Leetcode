class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bmap = [-2]*32
        bmap[0] = -1
        
        res = 0
        mask = 0
        
        for i in range(len(s)):
            if s[i] == 'a':
                mask = mask^1
            elif s[i] == 'e':
                mask = mask^2
            elif s[i] == 'i':
                mask = mask^4
            elif s[i] == 'o':
                mask = mask^8
            elif s[i] == 'u':
                mask = mask^16
        
            prev = bmap[mask]
            if prev == -2:
                bmap[mask] = i
            else:
                res = max(res, i - prev)
        
        return res