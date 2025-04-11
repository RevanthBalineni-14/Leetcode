class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def sum(num):
            cnum = 0
            for i in num:
                cnum = cnum*10 + int(i)
            num = cnum
            res = 0
            while num>0:
                res+= num%10
                num = num//10
            return res
        
        res = 0

        for i in range(low, high+1):
            if len(str(i))%2 == 0:
                clen = len(str(i))
                res += 1 if (sum(str(i)[:clen//2]) == sum(str(i)[clen//2:])) else 0
        
        return res