class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        mydic = defaultdict(int)
        
        for [i,j] in edges:
            mydic[j] += 1
        
        count = 0
        val = 0
        for i in range(n):
            if mydic[i] == 0:
                count += 1
                val = i
                
        if count == 1:
            return val
        else:
            return -1