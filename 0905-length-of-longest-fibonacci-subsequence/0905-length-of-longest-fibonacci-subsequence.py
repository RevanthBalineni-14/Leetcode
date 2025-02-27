class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if len(arr)<=2:
            return 0
        indexset = set()
        for i in (arr):
            indexset.add(i)
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                clen = 2
                prev, curr = arr[i], arr[j]
                while (prev+curr) in indexset:
                    clen+=1
                    res = max(clen, res)
                    curr, prev = curr+prev, curr

        return res if res>2 else 0
