import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v, cost in roads:
            adjList[u].append((v, cost))
            adjList[v].append((u, cost))

        dist = [float('inf')]*n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]
        mod = 10**9 + 7

        while pq:
            d, node = heapq.heappop(pq)
            if d>dist[node]:
                continue
            
            for neighbor, time in adjList[node]:
                if (dist[node] + time)<dist[neighbor]:
                    heapq.heappush(pq, (dist[node] + time, neighbor))
                    ways[neighbor] = ways[node]
                    dist[neighbor] = dist[node]+time
                elif dist[neighbor] == (dist[node]+time):
                    ways[neighbor] += ways[node]
            
        return ways[n-1]%mod