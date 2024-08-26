import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = [0] * len(w)
        self.prefix[0] = w[0]
        for i in range(1, len(w)):
            self.prefix[i] = w[i] + self.prefix[i - 1]

    def pickIndex(self) -> int:
        def binary_search(data, val):
            lo, hi = 0, len(data) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if data[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        rand = random.randint(1, self.prefix[-1])
        return binary_search(self.prefix, rand)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
