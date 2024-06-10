class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights
        heights = sorted(heights)
        count = 0
        for ind,i in enumerate(temp):
            if i!=heights[ind]:
                count += 1
        
        return count