class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        newl = list(zip(startTime, endTime, profit))
        newl.sort()
        @lru_cache(None)
        def rec(i):
            if(i==len(newl)):
                return 0
            j=i+1
            while j<len(newl) and newl[i][1]>newl[j][0] :
                j=j+1
            crtsum = newl[i][2] + rec(j)
            two= rec(i+1)
            return max(crtsum,two)
        return rec(0)