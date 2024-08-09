class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def checker(row, col, grid):
            seen = [False]*9
            for i in range(row, row+3):
                for j in range(col,col+3):
                    if grid[i][j]>9 or grid[i][j]<1 or seen[grid[i][j]-1]:
                        return False
                    seen[grid[i][j]-1] = True
                    
            csum = grid[row][col] + grid[row][col+1] + grid[row][col+2]
            
            for i in range(1,3):
                if csum != grid[row+i][col] + grid[row+i][col+1] + grid[row+i][col+2]:
                    return False
                
            for i in range(0,3):
                if csum != grid[row][col+i] + grid[row+1][col+i] + grid[row+2][col+i]:
                    return False
            if csum!= (grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]) or csum!= (grid[row+2][col] + grid[row+1][col+1] + grid[row][col+2]):
                return False
            return True
        
        
        res = 0 
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if checker(i, j, grid):
                    res+=1
                    
        return res               