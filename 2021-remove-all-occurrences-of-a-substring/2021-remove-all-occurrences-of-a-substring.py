class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def isSame(currString, ind):

            for i in range(len(part)):
                if (ind+i)<len(currString) and part[i] == currString[ind+i]:
                    continue
                else:
                    return False
            return True

        i = 0
        while i<len(s):
            if isSame(s, i):
                s = s[0:(i)]+ s[(i+len(part)):]
                i -= len(part)
                i = max(i, 0)
                continue
            i += 1
        
        return s