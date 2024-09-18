class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0' or '00' in s:
            return 0
        
        memo = {}
        def traverse(s, ind):
            if ind == len(s):
                return 1
            if s[ind] == '0':
                return 0
            if ind in memo:
                return memo[ind]
            
            
            res = traverse(s, ind+1)
            
            if ind+1<len(s) and 10<= int(s[ind:ind+2])<= 26:
                res += traverse(s, ind+2)
                
            memo[ind] = res
            
            return res
        
        return traverse(s, 0)
            