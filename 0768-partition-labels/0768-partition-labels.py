class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occurences = defaultdict(list)
        for ind, i in enumerate(s):
            if len(occurences[i])==0:
                occurences[i].append(ind)
                occurences[i].append(ind)
            else:
                occurences[i][1] = ind
        # print(occurences)
        intervals = []
        for key in occurences:
            intervals.append(occurences[key])
        intervals.sort()
        stack = []
        # print(intervals)
        for i in intervals:
            if stack and stack[-1][1]>i[0]:
                stack[-1][1] = max(stack[-1][1], i[1])
            else:
                stack.append(i)
        # print(stack) 
        res = [] 
        for i in stack:
            res.append(i[1]-i[0]+1)
        return res