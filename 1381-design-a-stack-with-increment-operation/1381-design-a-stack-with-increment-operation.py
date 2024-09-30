class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.arr = []

    def push(self, x: int) -> None:
        if len(self.arr) == self.maxSize:
            return
        self.arr.insert(0, x)

    def pop(self) -> int:
        if len(self.arr)==0:
            return -1
        return self.arr.pop(0)

    def increment(self, k: int, val: int) -> None:
        if k > len(self.arr):
            k = len(self.arr)
            
        for i in range(k):
            self.arr[len(self.arr)-1-i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)