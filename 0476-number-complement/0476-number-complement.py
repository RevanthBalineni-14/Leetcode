class Solution:
    def findComplement(self, num: int) -> int:
        nr = 0
        ct = 0
        while num>0:
            nr += abs(1-num%2)*(2**ct)
            num = num//2
            ct+=1
        
        return nr