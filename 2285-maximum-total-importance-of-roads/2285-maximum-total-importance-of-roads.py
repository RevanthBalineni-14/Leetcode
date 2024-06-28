class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count  = [0]*n
        
        for i in roads:
            count[i[0]] += 1
            count[i[1]] += 1
        hset = [0]*n
        for i in range(len(count)):
            hset[i] = (count[i], i)
        hset = sorted(hset, key = lambda x: x[0], reverse = True)
        res = 0
        crt=n
        for i in hset:
            res += crt*i[0]
            crt -= 1
        
        return res