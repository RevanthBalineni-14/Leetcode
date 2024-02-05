class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = set()
        ind = [10**6]*26
        for i in range(len(s)):
            if s[i] in vals:
                ind[ord(s[i])-97] = 10**6
                continue
            else:
                vals.add(s[i])
                ind[ord(s[i])-97] = i
        if min(ind)==10**6:
            return -1
        else:
            return min(ind)