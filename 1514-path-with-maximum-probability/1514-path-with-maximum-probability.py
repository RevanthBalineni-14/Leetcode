class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], succProb[i]])
            graph[edges[i][1]].append([edges[i][0], succProb[i]])
        
        max_heap = []
        heapq.heappush(max_heap, (-1, start_node))
        probabilities = [0]*n
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob
            
            if node == end_node:
                return prob
            
            for n, p in graph[node]:
                new_prob = prob*p
                if new_prob>probabilities[n]:
                    heapq.heappush(max_heap,(-new_prob, n))
                    probabilities[n] = new_prob
                    
        
        return 0