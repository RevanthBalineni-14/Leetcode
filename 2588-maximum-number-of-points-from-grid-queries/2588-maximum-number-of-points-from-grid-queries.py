import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        minheap = []
        queryheap = []
        for ind, val in enumerate(queries):
            heapq.heappush(queryheap, (val, ind))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                heapq.heappush(minheap, (grid[i][j], i, j))

        vis = [[False]*len(grid[0]) for _ in range(len(grid))]

        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        points = 0
        res = [0]*len(queries)
        nodeheap = [(grid[0][0], 0, 0)]
        vis[0][0] = True

        while len(queryheap)>0:
            val, ind = heapq.heappop(queryheap)
            while len(nodeheap)>0 and nodeheap[0][0]<val:
                points+=1
                _, cr, cc = heapq.heappop(nodeheap)
                for dr, dc in dirs:
                    tr = cr+dr
                    tc = cc+dc
                    if 0<=tr<len(grid) and 0<=tc<len(grid[0]) and vis[tr][tc] == False:
                        vis[tr][tc] = True
                        heapq.heappush(nodeheap, (grid[tr][tc], tr, tc))
                
            res[ind] = points

        return res