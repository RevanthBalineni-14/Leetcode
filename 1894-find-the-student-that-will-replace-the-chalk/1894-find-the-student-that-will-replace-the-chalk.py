class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        csum = sum(chalk)
        k = k%csum
        
        for i in range(len(chalk)):
            k-=chalk[i]
            if k<0:
                return i
            
        return 0