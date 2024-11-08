class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(0, 32):
            count = 0
            
            for c in candidates:
                if (c & 1<<i) > 0:
                    count += 1
            res = max(res, count)
        
        return res