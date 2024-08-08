class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i,j = rStart, cStart
        movei = 2
        cmoves = 1
        nmoves = 2
        dx, dy = 0, 1
        res = []
        while len(res) < rows*cols:
            if (-1<i<rows) and (-1<j<cols):
                res.append([i,j])
                
            i += dx
            j += dy
            
            cmoves -= 1
            
            if cmoves==0:
                dx, dy = dy, -dx
                movei -= 1
                if movei == 0:
                    movei = 2
                    cmoves = nmoves
                    nmoves += 1
                else:
                    cmoves = nmoves - 1
            
        return res