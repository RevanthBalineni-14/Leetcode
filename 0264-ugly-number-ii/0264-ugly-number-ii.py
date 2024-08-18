import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = [2,3,5]
        uh = [1]
        vis = set()
        vis.add(1)
        for  _ in range(n):
            curr = heappop(uh)
            for i in s:
                if i*curr not in vis:
                    heapq.heappush(uh, i*curr)
                    vis.add(i*curr)
        return curr