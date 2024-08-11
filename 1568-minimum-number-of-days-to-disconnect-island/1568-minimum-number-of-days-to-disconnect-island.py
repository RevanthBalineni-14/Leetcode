class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def counter():
            islands = 0
            seen = set()
            def dfs(r,c):
                st = [(r,c)]
                while st:
                    x, y = st.pop()
                    for i,j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0<= i <len(grid) and 0<= j <len(grid[0]) and grid[i][j]==1 and (i, j) not in seen:
                            seen.add((i, j))
                            st.append((i,j))
                            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and (i,j) not in seen:
                        islands +=1
                        seen.add((i, j))
                        dfs(i,j)
            
            return islands
        
        if counter()!=1:
            return 0
        
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        grid[i][j]=0
                        if counter() != 1:
                            return 1
                        grid[i][j]=1
        
        return 2
                        