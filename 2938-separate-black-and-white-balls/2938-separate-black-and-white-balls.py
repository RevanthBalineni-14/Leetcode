class Solution:
    def minimumSteps(self, s: str) -> int:
        precount = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                precount += 1
            else:
                res += precount
            
        return res