class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        mydic = {}
        for i in s:
            mydic[i] = mydic.get(i,0) + 1
        
        res = ""
        
        for i in range(mydic.get('1',0)-1):
            res += "1"
        
        for i in range(mydic.get('0',0)):
            res += "0"
        
        return res+"1"