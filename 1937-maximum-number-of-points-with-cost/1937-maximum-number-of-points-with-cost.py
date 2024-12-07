class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n  = len(points), len(points[0])
        prev = points[0]
        
        for row in range(1,m):
            left, right = [0]*n, [0]*n
            
            left[0], right[n-1] = prev[0], prev[n-1]-(n-1)
            
            for i in range(1, n):
                left[i] = max(left[i-1], prev[i]+i)
            
            for j in range(n-2, -1, -1):
                right[j]  = max(right[j+1], prev[j]-j)
            
            for c in range(n):
                prev[c] = points[row][c] + max(left[c]-c, right[c]+c)
        
        return max(prev)