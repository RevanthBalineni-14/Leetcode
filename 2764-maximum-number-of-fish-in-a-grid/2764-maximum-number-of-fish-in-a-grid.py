class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False]*n for _ in range(m)]
        igrid = [[0]*n for _ in range(m)]

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def isValid(i, j):
            if 0<=i<m and 0<=j<n:
                return True
            else:
                return False

        def traverse(crtno, i, j):
            if visited[i][j]:
                return
            if grid[i][j]==0:
                return 

            visited[i][j] = True
            igrid[i][j] = crtno
            for dx, dy in dirs:
                tx, ty = i+dx, j+dy
                if isValid(tx, ty):
                    traverse(crtno, tx, ty)

        icount = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0 and not visited[i][j]:
                    traverse(icount, i, j)
                    icount += 1

        islandsizes = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if igrid[i][j] !=0:
                    islandsizes[igrid[i][j]] += grid[i][j]

        res = 0
        for i in islandsizes:
            if islandsizes[i]>res:
                res = islandsizes[i]
        
        return res