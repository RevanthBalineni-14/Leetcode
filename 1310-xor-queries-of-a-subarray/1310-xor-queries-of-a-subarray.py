class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = []
        curr = 0
        
        for i in range(len(arr)):
            curr = curr^arr[i]
            prefix.append(curr)
            
        for i in queries:
            
            if i[0]<(i[1]-i[0]+1):
                curr = prefix[i[1]]
                for j in range(i[0]):
                    curr = curr^arr[j]
                res.append(curr)
            else:
                curr = 0
                for j in range(i[0], i[1]+1):
                    curr = curr ^ arr[j]        
                res.append(curr)
        return res