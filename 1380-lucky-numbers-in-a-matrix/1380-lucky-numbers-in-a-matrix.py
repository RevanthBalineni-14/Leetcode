from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(matrix)):
            minele = min(matrix[i])
            for j in range(len(matrix[0])):
                col = [matrix[row][j] for row in range(len(matrix))]
                if matrix[i][j] == minele and matrix[i][j] == max(col):
                    res.append(matrix[i][j])
                    
        return res
