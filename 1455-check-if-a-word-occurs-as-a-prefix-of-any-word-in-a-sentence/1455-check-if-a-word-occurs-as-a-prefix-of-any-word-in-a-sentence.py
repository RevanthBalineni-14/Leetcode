class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        n = len(searchWord)
        count = 1
        for i in sentence.split():
            if len(i)<n:
                count+=1
                continue
            elif i.startswith(searchWord):
                return count
            count+=1
        
        return -1