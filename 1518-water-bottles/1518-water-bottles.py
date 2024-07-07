class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        rem = 0
        prevrem = 0
        while(numBottles>0):
            res += numBottles
            rem = (numBottles+prevrem)%numExchange
            numBottles = (numBottles+prevrem)//numExchange
            prevrem = rem
            
        return res