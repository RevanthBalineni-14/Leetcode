class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, right, res = 0, 0, 0
        counta, countb, countc = 0, 0, 0
        for right in range(len(s)):
            if s[right]=='a':
                counta += 1
            elif s[right]=='b':
                countb += 1
            else:
                countc += 1
            while counta>0 and countb>0 and countc>0:
                res += len(s)-right
                if s[left]=='a':
                    counta -= 1
                elif s[left]=='b':
                    countb -= 1
                else:
                    countc -= 1
                left += 1
        return res