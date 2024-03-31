class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        dif = -1
        crt= prices[0]
        for i in range(1, len(prices)):
            dif = prices[i]-crt
            if dif<0:
                crt = prices[i]
            else:
                res = max(res, dif)
        
        return res