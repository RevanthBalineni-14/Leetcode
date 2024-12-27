class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        st = []
        heapq.heappush(st, -values[0])
        
        for i in range(1, len(values)):
            res = max(res, -st[0]+values[i]-i)
            heapq.heappush(st, -(i+values[i]))
            
        return res