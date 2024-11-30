class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(deque)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        
        for st, end in pairs:
            graph[st].append(end)
            indeg[end] += 1
            outdeg[st] += 1
        
        start = pairs[0][0]
        for node in graph:
            if outdeg[node] > indeg[node]:
                start = node
                break
        
        st = [start]
        res = []
        
        while st:
            while graph[st[-1]]:
                nxt = graph[st[-1]].popleft()
                st.append(nxt)
            
            res.append(st.pop())
        
        res.reverse()
        return [[res[i], res[i + 1]] for i in range(len(res) - 1)]
                