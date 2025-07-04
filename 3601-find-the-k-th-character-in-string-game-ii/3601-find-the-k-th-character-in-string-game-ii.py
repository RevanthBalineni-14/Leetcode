class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cnt = 0
        n = len(operations)
        mid = 2**(n-1)
        while n>0:
            if k>mid:
                k = k-mid
                if operations[n-1] == 1:
                    cnt += 1
            mid = mid//2
            n-=1
        return chr(ord('a') + cnt%26)