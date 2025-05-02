class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        st = []
        lprefix = []
        for i in range(len(dominoes)):
            if not st or st[-1][0]=='L':
                lprefix.append(-1)
            else:
                lprefix.append(st[-1][1])
            if dominoes[i]=='L' or dominoes[i]=='R':
                st.append((dominoes[i], i))
        st = []
        rprefix = []
        for i in range(len(dominoes)-1, -1, -1):
            if not st or st[-1][0]=='R':
                rprefix.append(-1)
            else:
                rprefix.append(st[-1][1])
            if dominoes[i]=='L' or dominoes[i]=='R':
                st.append((dominoes[i], i))
        rprefix = rprefix[::-1]
        
        res = []
        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                res.append(dominoes[i])
                continue

            if lprefix[i] == -1:
                ldist = float('inf')
            else:
                ldist = i-lprefix[i]

            if rprefix[i] == -1:
                rdist = float('inf')
            else:
                rdist = rprefix[i]-i
            
            if ldist == rdist:
                res.append('.')
            elif ldist<rdist:
                res.append('R')
            else:
                res.append('L')
        
        return ''.join(res)