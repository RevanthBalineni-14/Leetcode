class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        st, end = 0, len(tokens)-1
        s = 0
        res = 0
        while st<=end:
            if power>=tokens[st]:
                power -= tokens[st]
                s+=1
                st+=1
                res = max(res, s)
            elif s>0:
                power +=tokens[end]
                s -= 1
                end -= 1
            else:
                break
        
        return res