class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0' or '00' in s:
            return 0
        
        memo = {}
        def single(i):
            if i=='*':
                return 9
            elif i == '0':
                return 0
            else:
                return 1
            
        def double(a, b):
            if a == '*' and b == '*':
                return 15
            elif a == '*':
                if '0' <= b <= '6':
                    return 2
                elif '7' <= b <='9':
                    return 1
                else:
                    return 0
            elif b == '*':
                if a == '1':
                    return 9
                elif a == '2':
                    return 6
                else:
                    return 0
            else:
                if a=='0':
                    return 0
                if 10 <= int(a+b) <= 26:
                    return 1
                else:
                    return 0
                
                    
        def traverse(s, ind):
            if ind == len(s):
                return 1
            if s[ind] == '0':
                return 0
            if ind in memo:
                return memo[ind]
            
            
            res = single(s[ind])*traverse(s, ind+1)
            res = res%(10**9+7)
            
            if ind+1<len(s):
                res += double(s[ind], s[ind+1])*traverse(s, ind+2)
                res = res%(10**9+7)
                
            memo[ind] = res
            
            return res
        
        return traverse(s, 0)
            