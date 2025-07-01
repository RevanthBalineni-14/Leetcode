class Solution:
    def possibleStringCount(self, word: str) -> int:
        cc, res = 1, 1
        for i in range(1, len(word)):
            if word[i]==word[i-1]:
                cc += 1
            else:
                res += cc-1
                cc = 1
        res += cc-1
        return res