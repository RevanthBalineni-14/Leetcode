class Solution:
    def longestPalindrome(self, s: str) -> int:
        hs = set()
        for i in s:
            if i in hs:
                hs.remove(i)
            else:
                hs.add(i)
        return len(s)-len(hs) + 1 if len(hs)>0 else len(s)