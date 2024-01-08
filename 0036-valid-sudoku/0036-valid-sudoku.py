class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res=[]
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != "." :
                    if (i, val) in res or (val, j) in res or (i//3, j//3, val) in res:
                        return False
                    res.append((i, val))
                    res.append((val, j))
                    res.append((i//3, j//3, val))
        
        return True