import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        endingtimeheap = []
        maxval = 0
        
        res = max([x[2] for x in events])
        # print([x[2] for x in events])
        for i in range(len(events)):
            st, end, val = events[i]
            while endingtimeheap and endingtimeheap[0][0]<st:
                maxval = max(maxval, endingtimeheap[0][1])
                heapq.heappop(endingtimeheap)
                
            heapq.heappush(endingtimeheap, (end, val))
            res = max((val + maxval), res)
        
        return res