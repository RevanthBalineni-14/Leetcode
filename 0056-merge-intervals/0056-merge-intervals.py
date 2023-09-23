class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key = lambda i : i[0])
        result=[intervals[0]]
        for i in intervals[1:]:
            latest=result[-1]
            if latest[1]>=i[0]:
                result[-1][1]=max(latest[1],i[1])
            else:
                result.append(i)
        return result