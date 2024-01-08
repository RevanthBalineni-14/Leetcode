class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res=[]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != "." :
                    if (i, val) in res or (val, j) in res or (i//3, j//3, val) in res:
                        return False
                    res.append((i, val))
                    res.append((val, j))
                    res.append((i//3, j//3, val))
        
        return True