class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
# there can be atmost 2 MHTS in the case the adjacent nodes are midpoints in the longest path of the tree
        if n==1:
            return [0]
        graph = defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        leaves = deque([i for i in range(n) if len(graph[i])==1])

        while n>2:
            n=n-len(leaves)
            ct=len(leaves)
            for i in range(ct):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)