class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            if (1<<i & start) != (1<<i & goal):
                res += 1
                
        return res