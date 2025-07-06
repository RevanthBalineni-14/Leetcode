from collections import Counter

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2Counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        cval = self.nums2[index]
        self.nums2Counter[cval] -= 1
        if self.nums2Counter[cval] <= 0:
            self.nums2Counter.pop(cval)
        self.nums2[index] += val
        self.nums2Counter[cval+val] += 1
        
    def count(self, tot: int) -> int:
        res = 0
        for val in self.nums1:
            res += self.nums2Counter[tot-val]
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)