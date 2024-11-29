class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        m, n = len(grid), len(grid[0])
        h = []
        heapq.heappush(h, (0, 0, 0))
        tx, ty = m-1, n-1
        vis = [[False]*n for _ in range(m)]
        if grid[0][0] > 0:
            return -1
        if (m > 1 and grid[1][0] > 1) and (n > 1 and grid[0][1] > 1):
            return -1
        
        while h:
            ct, cx, cy = heapq.heappop(h)
            if vis[cx][cy]:
                continue
                
            vis[cx][cy] = True
            
            if cx == tx and cy == ty:
                return ct
            
            for d in dirs:
                dx, dy = cx+d[0], cy+d[1]
                
                if -1<dx and dx<m and -1<dy and dy<n and not vis[dx][dy]:
                    if (ct+1)<grid[dx][dy]:
                        if cx==0 and cy==0 and grid[0][1]>1 and grid[1][0]>1:
                            continue
                        if (grid[dx][dy]-ct)%2==0:
                            heapq.heappush(h, (grid[dx][dy]+1, dx, dy))
                        else:
                            heapq.heappush(h, (grid[dx][dy], dx, dy))
                                
                    else:
                        heapq.heappush(h, (ct+1, dx, dy))
        
        return -1