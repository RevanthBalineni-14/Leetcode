class MedianFinder:
    mylist = []
    def __init__(self):
        self.mylist = []

    def addNum(self, num: int) -> None:
        self.mylist.append(num)

    def findMedian(self) -> float:
        self.mylist.sort()
        if len(self.mylist) == 1:
            return self.mylist[0]
        mid = len(self.mylist)//2
        if len(self.mylist)%2==0:
            return (self.mylist[mid]+self.mylist[mid-1])/2
        else:
            return self.mylist[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()