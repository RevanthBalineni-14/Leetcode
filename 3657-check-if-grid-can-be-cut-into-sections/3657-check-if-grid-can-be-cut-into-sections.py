class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(intervals):
            intervals.sort()
            cmax = intervals[0][1]
            boundaries = 0
            for start, end in intervals[1:]:
                if start>=cmax:
                    boundaries += 1
                
                cmax = max(cmax, end)
            
            return boundaries>=2
        
        x_intervals = [(r[0], r[2]) for r in rectangles]
        y_intervals = [(r[1], r[3]) for r in rectangles]
        
        return check(x_intervals) or check(y_intervals)