class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        mydic = {}
        for i in s:
            mydic[i] = mydic.get(i,0) + 1
        
        return "1"*(mydic.get('1',0)-1)+"0"*mydic.get('0',0)+"1"