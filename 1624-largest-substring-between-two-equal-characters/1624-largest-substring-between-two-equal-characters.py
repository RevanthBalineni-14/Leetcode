class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxl = -1
        idarr = [-1]*26
        for i in range(0,len(s)):
            if idarr[ord(s[i])-ord('a')]!=-1:
                crt = i - idarr[ord(s[i])-ord('a')]-1
                maxl = max(maxl, crt)
            else:
                idarr[ord(s[i])-ord('a')]=i
                
        return maxl