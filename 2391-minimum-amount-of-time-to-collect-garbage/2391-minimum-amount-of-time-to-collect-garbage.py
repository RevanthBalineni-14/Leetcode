class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        parr = [None]*len(garbage)
        parr[0] = 0
        for i in range(1, len(parr)):
            parr[i] = parr[i-1] + travel[i-1]
        
        gp, pp, mp = 0, 0, 0 
        res = 0
        for i in range(0, len(garbage)):
            if "G" in garbage[i]:
                res += garbage[i].count("G") + parr[i] - parr[gp]
                gp = i
            
            if "P" in garbage[i]:
                res += garbage[i].count("P") + parr[i] - parr[pp]
                pp = i

            if "M" in garbage[i]:
                res += garbage[i].count("M") + parr[i] - parr[mp]
                mp = i
        
        return res