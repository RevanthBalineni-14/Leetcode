class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findBit(n, k):
            if n==1:
                return '0'
            
            length = (1 << n) -1
            
            middle = length // 2 + 1
            
            if k == middle:
                return '1'
            elif k < middle:
                return findBit(n-1, k)
            else:
                mp = length - k + 1
                bit = findBit(n-1, mp)
                return '0' if bit == '1' else '1'
        
        return findBit(n, k)