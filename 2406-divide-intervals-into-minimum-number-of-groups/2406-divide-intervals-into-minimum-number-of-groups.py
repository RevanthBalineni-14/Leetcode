import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        end_heap = []
        
        for i in intervals:
            if end_heap and end_heap[0] < i[0]:
                heapq.heapreplace(end_heap, i[1])
            else:
                heapq.heappush(end_heap, i[1])
        
        return len(end_heap)
