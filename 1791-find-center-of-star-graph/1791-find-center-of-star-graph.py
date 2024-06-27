class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        count = [0]*(n+2)
        
        for i in edges:
            for j in i:
                count[j] += 1
        
        maxi, maxv =-1, -1
        
        for ind, i in enumerate(count):
            if i>maxv:
                maxv = i
                maxi = ind
            
        return maxi