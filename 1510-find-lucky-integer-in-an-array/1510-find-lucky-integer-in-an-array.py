from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arrcounter = Counter(arr)
        cmax = 0
        for key in arrcounter:
            if arrcounter[key] == key:
                cmax = max(cmax, key)
        return cmax if cmax>0 else -1