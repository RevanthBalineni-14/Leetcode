from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mydic = {}
        for i in arr:
            mydic[i] = mydic.get(i, 0) + 1
        sorted_freq = sorted(mydic.items(), key=lambda x: x[1])
        ct = len(sorted_freq)
        for _, freq in sorted_freq:
            k -= freq
            if k < 0:
                break
            ct -= 1
        
        return ct
