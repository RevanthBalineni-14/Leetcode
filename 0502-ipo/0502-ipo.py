class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(profits, capital), key = lambda l: l[1])
        i = 0 
        for _ in range(k):
            
            while i<len(projects) and w>=projects[i][1]:
                heapq.heappush(heap, -projects[i][0])
                i+=1
            
            if heap:
                w -= heapq.heappop(heap)
            else:
                break
        
        return w