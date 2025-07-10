class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0]]
        for i in range(1, len(startTime)):
            gaps.append(startTime[i]-endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        prefixarr = [gaps[0]]
        for i in range(1, len(gaps)-1):
            prefixarr.append(max(prefixarr[-1], gaps[i]))

        suffixarr = [gaps[-1]]
        for i in range(len(gaps)-2, 0, -1):
            suffixarr.append(max(suffixarr[-1], gaps[i]))
        suffixarr = list(reversed(suffixarr))

        ans, N = 0, len(startTime)

        for i, (start, end) in enumerate(zip(startTime, endTime)):
            slot = end - start
            left, right = gaps[i], gaps[i+1]
            time = left+right
            bestleftgap = -1 if i==0 else prefixarr[i-1]
            bestrightgap = -1 if i == (N-1) else suffixarr[i+1]

            if bestleftgap>=slot or bestrightgap>=slot:
                time += slot
            ans = max(ans, time)
        
        return ans