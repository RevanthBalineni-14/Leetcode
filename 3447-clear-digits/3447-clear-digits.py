class Solution:
    def clearDigits(self, s: str) -> str:
        cset = {"0","1", "2", "3","4","5","6","7","8","9"}
        while True:
            flag = 0
            for i in range(1, len(s)):
                if s[i] in cset and s[i-1] not in cset:
                    s = s[:i-1]+s[i+1:]
                    flag = 1
                    break
            if flag==1:
                continue
            return s
        return s