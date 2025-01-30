class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        self.adj = [[] for _ in range(n)]
        for x,y in edges:
            self.adj[x-1].append(y-1)
            self.adj[y-1].append(x-1)

        self.components = []
        self.fill_components(n)

        res = 0
        for comp in self.components:
            comp_ans = 0
            if self.bipartitecheck(comp[0], comp):
                for i in range(len(comp)):
                    comp_ans = max(comp_ans, self.bfs(comp[i], n))
                res += comp_ans
            else:
                return -1

        return res
    
    def bfs(self, start, n):
        res = 0
        vis = [False]*n
        q = deque([start])
        vis[start] = True
        while q:
            res+=1
            for _ in range(len(q)):
                curr = q.popleft()
                for neigh in self.adj[curr]:
                    if not vis[neigh]:
                        vis[neigh] = True
                        q.append(neigh)
        return res

    def bipartitecheck(self, start, comp):
        color = {node: -1 for node in comp}
        q=deque([start])
        color[start] = 0

        while q:
            curr = q.popleft()
            for i in self.adj[curr]:
                if color[i] == -1:
                    color[i] = 1 - color[curr]
                    q.append(i)
                elif color[i]==color[curr]:
                    return False
        
        return True

    def fill_components(self, n):
        vis = [False]*n
        def bfs(start):
            vis[start] = True
            tmp = []
            q = deque()
            q.append(start)
            while q:
                curr = q.popleft()
                tmp.append(curr)
                for val in self.adj[curr]:
                    if not vis[val]:
                        q.append(val)
                        vis[val] = True
            
            return tmp
        
        for i in range(n):
            if not vis[i]:
                tmp = bfs(i)
                self.components.append(tmp)