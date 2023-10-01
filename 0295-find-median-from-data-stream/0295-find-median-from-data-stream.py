class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap=[]

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if not len(self.max_heap) or num <= self.min_heap[0]:
                heapq.heappush(self.max_heap,-1*num)
            else:
                heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap)) 
                heapq.heappush(self.min_heap, num)
        else:
            if num>= abs(self.max_heap[0]):
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -1*num)

    def findMedian(self) -> float:
        if (len(self.min_heap)+len(self.max_heap))%2==1:
            return -1*self.max_heap[0]
        
        return (-1*self.max_heap[0]+1*self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()