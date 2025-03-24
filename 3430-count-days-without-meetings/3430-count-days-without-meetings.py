class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = []
        for meeting in meetings:
            if merged and merged[-1][1]>=meeting[0]:
                merged[-1][1] = max(merged[-1][1], meeting[1])
            else:
                merged.append(meeting)
        
        bookeddays = 0
        for meeting in merged:
            bookeddays += meeting[1]-meeting[0]+1
        return days-bookeddays