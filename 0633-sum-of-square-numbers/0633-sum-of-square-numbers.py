class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(c**(0.5))
        l = 0
        while l<=r:
            if (l**2+r**2)==c:
                return True
            if (l**2+r**2)<c:
                l += 1
            else:
                r-=1
        return False