class Solution:
    def reverseParentheses(self, s: str) -> str:
        crt = 0
        res = ""
        ob = []
        for i in s:
            
            if i == "(":
                ob.append(crt)
            elif i == ")":
                res = res[:ob[-1]] + (res[ob[-1]:])[::-1]
                ob.pop()
            else:
                res += i
                crt += 1
                
        return res