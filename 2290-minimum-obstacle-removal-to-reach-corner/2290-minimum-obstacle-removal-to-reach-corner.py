class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        m, n = len(grid), len(grid[0])
        q = deque()
        cx, cy = 0, 0 
        tx, ty = m-1, n-1
        if m == 1 and n == 1:
            return grid[0][0]

        q.append([cx, cy, grid[0][0]])
        vis = [[False]*n for _ in range(m)]
        vis[0][0] = True
        while q:
            cx, cy, moves = q.popleft()
            if cx == tx and cy == ty:
                return moves
        
            for d in dirs:
                dx, dy = cx+d[0], cy+d[1]
                if -1<dx and dx<m and -1<dy and dy<n and not vis[dx][dy]:
                    vis[dx][dy] = True
                    if grid[dx][dy]==1:
                        q.append([dx, dy, moves+grid[dx][dy]])
                    else:
                        q.appendleft([dx, dy, moves])
                    
        return -1