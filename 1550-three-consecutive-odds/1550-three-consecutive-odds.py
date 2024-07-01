class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ct = 0
        for i in arr:
            if i%2==1:
                ct+=1
                if ct>=3:
                    return True
            else:
                ct = 0
        
        return False