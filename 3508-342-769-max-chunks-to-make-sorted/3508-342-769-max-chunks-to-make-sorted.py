class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_heap = []
        res = 0
        for i in range(len(arr)):
            if not max_heap:
                max_heap.append(-arr[i])
                res += 1
                continue
            
            if -max_heap[0] > arr[i]:
                res += 1
                temp = -max_heap[0]
                while max_heap and -max_heap[0] > arr[i]:
                    heapq.heappop(max_heap)
                    res -= 1
                heapq.heappush(max_heap, -temp)
            else:
                res += 1
                heapq.heappush(max_heap, -arr[i])

        return res