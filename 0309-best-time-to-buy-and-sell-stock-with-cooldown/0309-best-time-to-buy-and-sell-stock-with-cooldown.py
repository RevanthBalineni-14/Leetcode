class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        dp={}
        
        def exhaust(i, state):
            if(i>=len(prices)):
                return 0
            
            if (i,state) in dp:
                return dp[(i,state)]
            
            cooldown = exhaust(i+1,state)
            
            if state:
                buy=exhaust(i+1,not state)-prices[i]
                dp[i,state]=max(buy,cooldown)
            else:
                sell=exhaust(i+2,not state)+prices[i]
                dp[i,state]=max(cooldown,sell)
            
            return dp[(i,state)]
        
        return exhaust(0,True)