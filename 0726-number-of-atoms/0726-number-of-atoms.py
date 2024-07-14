class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st = [{}]
        
        i, n = 0, len(formula)
        while i<n:
            if formula[i] == '(':
                st.append({})
                i += 1
                
            elif formula[i] == ')':
                top = st.pop()
                i += 1
                i_start = i
                while i<n and formula[i].isdigit():
                    i+=1
                mul = int(formula[i_start:i] or 1)
                for ele, ct in top.items():
                    st[-1][ele] = st[-1].get(ele, 0) + ct*mul
            else:
                i_start = i
                i += 1
                while i<n and formula[i].islower():
                    i += 1
                ele = formula[i_start:i]
                i_start = i 
                while i<n and formula[i].isdigit():
                    i += 1
                ct = int(formula[i_start:i] or 1)
                st[-1][ele] = st[-1].get(ele, 0) + ct
        
        res = st.pop()
        sortres = sorted(res.keys())
        return ''.join(f"{ele}{(res[ele] if res[ele]>1 else '')}" for ele in sortres)