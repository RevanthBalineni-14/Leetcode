from bisect import bisect_left

class MyCalendarTwo:

    def __init__(self):
        self.sb = []
        self.db = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.db:
            if max(start, i) < min(j, end):
                return False
        
        for i, j in self.sb:
            if max(start, i) < min(j, end):
                self.db.append((max(start, i), min(j, end)))
        
        self.sb.append((start,end))
        return True