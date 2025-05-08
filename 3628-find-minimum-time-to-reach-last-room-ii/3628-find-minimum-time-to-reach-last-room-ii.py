import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dp = [[float('inf')] * m for _ in range(n)]
        minHeap = [(0, 0, 0, 0)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minHeap:
            currTime, currMoves, currX, currY = heapq.heappop(minHeap)
            if currTime>=dp[currX][currY]:
                continue
            
            dp[currX][currY] = currTime

            if currX==n-1 and currY==m-1:
                return currTime

            currMoves += 1

            for d in dirs:
                tempX, tempY = currX + d[0], currY + d[1]
                if tempX>-1 and tempX<n and tempY<m and tempY>-1 and dp[tempX][tempY]==float('inf'):
                    nextTime = max(moveTime[tempX][tempY], currTime) + (1 if (currMoves%2)==1 else 2)
                    heapq.heappush(minHeap, (nextTime, currMoves, tempX, tempY))
        return -1