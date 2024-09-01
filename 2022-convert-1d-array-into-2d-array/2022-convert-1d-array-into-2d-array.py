class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = [[] for _ in range(m)]
        if m*n!=len(original):
            return []
        for i in range(m):
            for j in range(n):
                if i*n+j<len(original):
                    res[i].append(original[i*n+j])
        
        return res