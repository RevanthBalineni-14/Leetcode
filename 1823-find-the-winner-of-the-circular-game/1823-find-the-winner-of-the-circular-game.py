class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        curr = 0
        while len(arr)!=1:
            nxt = (curr + k -1)%len(arr)
            arr.pop(nxt)
            curr = nxt
        
        return arr[0]