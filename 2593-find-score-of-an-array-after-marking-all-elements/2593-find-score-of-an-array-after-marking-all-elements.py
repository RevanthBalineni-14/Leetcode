class Solution:
    def findScore(self, nums: List[int]) -> int:
        myset = set()
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        res = 0
        while heap:
            cnum, ind = heapq.heappop(heap)
            if ind not in myset:
                res += cnum
                myset.add(ind+1)
                myset.add(ind)
                myset.add(ind-1)
        
        return res