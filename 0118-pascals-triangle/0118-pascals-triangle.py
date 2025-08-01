class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows ==2:
            return [[1], [1,1]]
        res = [[1], [1,1]]

        for i in range(3, numRows+1):
            prevRow = res[-1]
            newl = len(prevRow)+1
            newRow = [1 for _ in range(newl)]
            for j in range(1, newl-1):
                newRow[j] = prevRow[j-1] + prevRow[j]
            res.append(newRow)
        
        return res