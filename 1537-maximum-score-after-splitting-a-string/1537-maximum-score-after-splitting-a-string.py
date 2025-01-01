class Solution:
    def maxScore(self, s: str) -> int:
        onec, zeroc = 0, 0
        for i in s:
            if i == '1':
                onec += 1
            else:
                zeroc += 1
        crto, crtz = 0, 0
        res = 0
        for i in range(len(s)):
            if s[i] == '1':
                crto += 1
            else:
                crtz += 1
            if i<(len(s)-1):
                res = max(res, crtz + onec - crto)
        
        return res