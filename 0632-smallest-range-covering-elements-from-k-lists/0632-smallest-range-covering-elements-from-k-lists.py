import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        
        cmax = float("-inf")
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            cmax = max(cmax, nums[i][0])
            
        sm_range = [-2*10**5, 2*10**5]
        
        while min_heap:
            val, n_ind, arr_ind = heapq.heappop(min_heap)
            if cmax - val < sm_range[1]-sm_range[0]:
                sm_range = [val, cmax]
            
            if arr_ind == len(nums[n_ind])-1:
                break
            
            next_elem = nums[n_ind][arr_ind+1]
            heapq.heappush(min_heap, (next_elem, n_ind, arr_ind+1))
            
            cmax = max(cmax, next_elem)
        
        return sm_range