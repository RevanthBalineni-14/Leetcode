class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evenpos = n//2 + n%2
        oddpos = n//2
        def calcPower(number, power):
            if power == 0:
                return 1
            if power == 1:
                return number
            half = calcPower(number, power//2)
            remainder = power%2
            res = (half*half)%(10**9+7)
            if remainder>0:
                res = (res*number)%(10**9+7)
            return res

        primes = 4
        eves = 5
        res = ((calcPower(eves, evenpos))*(calcPower(primes, oddpos)))%(10**9 + 7)
        return res