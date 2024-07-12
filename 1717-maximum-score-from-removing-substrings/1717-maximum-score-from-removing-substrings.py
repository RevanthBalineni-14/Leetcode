class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x>y:
            t, ts = "ab", x
            b, bs = "ba", y
        else:
            t, ts = "ba", y   
            b, bs = "ab", x
        res = 0  
        st = []
        
        for i in s:
            if i == t[1] and st and st[-1] == t[0]:
                st.pop()
                res += ts
            else:
                st.append(i)
        
        newst = []
        
        for i in st:
            if i == b[1] and newst and newst[-1] == b[0]:
                newst.pop()
                res += bs
            else:
                newst.append(i)
                
        return res