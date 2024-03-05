class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = len(s)-1
        while start<end and s[start] == s[end]:
            c = s[start]
            while start<=end and c == s[start]:
                start+= 1
            
            while start<=end and c == s[end]:
                end -= 1
        
        return (end-start+1)