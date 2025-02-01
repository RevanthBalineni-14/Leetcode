class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        res = [[-1]*n for _ in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        queue = deque()

        for i in range(m):
             for j in range(n):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    queue.append((i, j))

        def isValid(x, y):
            if 0<=x<m and 0<=y<n:
                return True
            
            return False

        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                tx = x + dx
                ty = y + dy
                if isValid(tx, ty) and res[tx][ty] == -1:
                    res[tx][ty] = res[x][y] + 1
                    queue.append((tx, ty))
        
        return res