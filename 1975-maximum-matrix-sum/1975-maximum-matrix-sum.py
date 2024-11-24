class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minval = float('inf')
        count = 0 
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res += abs(matrix[i][j])
                if matrix[i][j]<0:
                    count += 1
                minval = min(minval, abs(matrix[i][j]))
            
        
        if count%2==1:
            res -= 2*minval
        
        return res