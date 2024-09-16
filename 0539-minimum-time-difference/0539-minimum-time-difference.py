class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            h, m = time.split(':')
            return int(h)*60+int(m)
        
        carr = map(convert, timePoints)
        carr=list(carr)
        carr.sort()
        res = 1440
        
        if (carr[0]+1440-carr[-1])<res:
                res = carr[0]+1440-carr[-1]
                
        for i in range(len(carr)-1):
            if carr[i+1]-carr[i]<res:
                res = carr[i+1]-carr[i]
            if (carr[i]+1440-carr[i+1])<res:
                res = carr[i]+1440-carr[i+1]
                
        return res