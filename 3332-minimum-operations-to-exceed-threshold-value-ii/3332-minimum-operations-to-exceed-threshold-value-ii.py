import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while nums[0]<k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            newval = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, newval)
            res +=1
        
        return res