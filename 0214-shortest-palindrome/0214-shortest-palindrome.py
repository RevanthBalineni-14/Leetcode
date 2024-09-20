class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s=="":
            return s
        def pallindromechecker(s):
            if s==s[::-1]:
                return True
            else:
                return False
        
        prefix = ""
        n = len(s)
        for prefind in range(n-1, -1, -1):
            if pallindromechecker(prefix+s):
                return prefix+s
            
            prefix += s[prefind]
            
        return s+s