class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        nex = [-1]*n
        stack = []
        for i, x in enumerate(heights):
            while stack and x > stack[-1][0]:
                nex[stack[-1][1]] = i
                stack.pop()
            stack.append((x, i))
        logn = 1
        while (1 << logn) < n:
            logn += 1

        # up - structure for binary lifting
        up = [[-1 for _ in range(logn+1)] for _ in range(n)]
        for i in reversed(range(n)):
            if nex[i] == -1: continue
            up[i][0] = nex[i]
            for j in range(1, logn+1):
                if up[i][j-1] == -1:
                    break
                up[i][j] = up[up[i][j-1]][j-1]

        # length of path from given node to the root
        @cache
        def get_len(i):
            if nex[i] == -1:
                return 1
            return 1 + get_len(nex[i])

        # make "ind" jumps from node "i" using binary lifting
        def get(i, ind):
            if ind == 0:
                return i
            cur = i
            for j in reversed(range(logn+1)):
                if ind & (1 << j):
                    cur = up[cur][j]
            return cur

        ans = []
        for a, b in queries:
            left = min(a, b)
            right = max(a, b)
            if left == right or heights[right] > heights[left]:
                ans.append(right)
                continue

            length = get_len(right)
            l = 0
            r = length
            while r - l > 1:
                m = l + (r - l) // 2
                heights_ind = get(right, m)
                if heights[heights_ind] <= heights[left]:
                    l = m
                else:
                    r = m
            heights_ind = get(right, r)
            if heights_ind == -1 or heights[heights_ind] <= heights[left]:
                ans.append(-1)
            else:
                ans.append(heights_ind)
        return ans