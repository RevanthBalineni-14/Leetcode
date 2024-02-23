class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        mydic = collections.defaultdict(dict)
        for f,t,p in flights:
            mydic[f][t] = p
        
        pq = [(0, src, k+1)]
        vis = [0]*n
        while pq:
            w, s, nd = heapq.heappop(pq)
            if s==dst:
                return w
            if vis[s]>=nd:
                continue
            vis[s] = nd
            for y, dw in mydic[s].items():
                heapq.heappush(pq, (w+dw, y, nd-1))
        return -1