class Solution:
    def maxDistance(self, arrays):
        min_heap = []
        max_heap = []

        # Build min heap and max heap
        for i, array in enumerate(arrays):
            heapq.heappush(min_heap, (array[0], i))
            heapq.heappush(max_heap, (-array[-1], i)) 

        max_distance = 0

        min_val, min_idx = heapq.heappop(min_heap)
        max_val, max_idx = heapq.heappop(max_heap)

        # Convert max_val back to positive
        max_val = -max_val

        # If they belong to different arrays, calculate the distance
        if min_idx != max_idx:
            return abs(max_val-min_val)
        else:
            new_min, _ = heapq.heappop(min_heap)
            new_max, _ = heapq.heappop(max_heap)
            new_max = -new_max
            return max(abs(new_max-min_val), abs(max_val - new_min))
        