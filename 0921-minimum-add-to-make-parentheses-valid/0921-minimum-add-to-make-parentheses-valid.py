class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        res = 0 
        for i in s:
            if i == ')' and len(st)>0 and st[-1] == '(':
                st.pop()
            elif i == '(':
                st.append(i)
            else:
                res += 1
        
        res += len(st)
        return res
            