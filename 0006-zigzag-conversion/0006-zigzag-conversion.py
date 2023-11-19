class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>len(s):
            return s
        rowele = [[] for _ in range(numRows)]
        ci, step  = 0, 1
        for i in range(len(s)):
            rowele[ci].append(s[i])
            if ci == 0:
                step = 1
            if ci == numRows-1:
                step = -1
            ci += step
        
        for i in range(len(rowele)):
            rowele[i] = "".join(rowele[i])
        
        return "".join(rowele)
