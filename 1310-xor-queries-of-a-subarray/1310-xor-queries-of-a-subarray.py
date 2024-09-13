class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = []
        curr = 0
        
        for i in range(len(arr)):
            curr = curr^arr[i]
            prefix.append(curr)
            
        for i in queries:       
            res.append(prefix[i[0]-1]^prefix[i[1]] if i[0]-1>-1 else prefix[i[1]])
        return res