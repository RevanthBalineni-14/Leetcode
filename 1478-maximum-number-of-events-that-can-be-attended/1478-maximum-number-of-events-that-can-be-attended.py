import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key = lambda x: x[0])
        h = []
        curr = 0
        res = 0
        for i in range(1, 100001):
            while h and h[0]<i:
                heapq.heappop(h)
            while curr<len(events) and events[curr][0]==i:
                heapq.heappush(h, events[curr][1])
                curr+=1
            if h:
                heapq.heappop(h)
                res+=1
        return res