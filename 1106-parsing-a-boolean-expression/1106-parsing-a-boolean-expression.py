class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for i in expression:
            if i in [',', '(']:
                continue
            
            if i in ['t', 'f', '&', '|', '!']:
                st.append(i)
            
            if i == ')':
                has_t = False
                has_f = False
                while st[-1] not in ['&', '|', '!']:
                    temp = st.pop()
                    if temp == 't':
                        has_t = True
                    else:
                        has_f = True
                op = st.pop()
                if op == '&':
                    st.append('f' if has_f else 't')
                elif op == '|':
                    st.append('t' if has_t else 'f')
                else:
                    st.append('t' if not has_t else 'f')
        
        return st[-1] == 't'
                
