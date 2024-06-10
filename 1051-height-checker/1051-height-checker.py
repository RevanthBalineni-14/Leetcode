class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freqheight = [0]*101
        for i in heights:
            freqheight[i] += 1
        
        crt, count = 0, 0
        for i in heights:
            
            while freqheight[crt] == 0:
                crt += 1
            
            freqheight[crt] -= 1
            
            if crt!=i:
                count += 1
        
        return count