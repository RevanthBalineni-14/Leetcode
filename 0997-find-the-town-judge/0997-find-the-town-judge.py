class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        cmax = 0
        cind = 0
        indeg = [0]*n
        outdeg = [0]*n
        for i in trust:
            indeg[i[1]-1] += 1
            outdeg[i[0]-1] += 1
            if indeg[i[1]-1] > cmax:
                cind = i[1]-1
                cmax = indeg[i[1]-1]
        
        if cmax==n-1:
            if outdeg[cind] == 0:
                return (cind+1)
        
        return -1