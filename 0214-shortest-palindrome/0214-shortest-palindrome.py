class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s=="":
            return s
        n = len(s)
        revs = s[::-1]
        for i in range(n):
            if s.startswith(revs[i:]):
                return revs[:i]+s

        return s+s