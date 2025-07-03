class Solution:
    def kthCharacter(self, k: int) -> str:
        curr = 'a'
        while len(curr)<k:
            newcurr = curr
            for i in curr:
                newcurr += chr(ord(i) + 1)
            curr = newcurr
        return curr[k-1]