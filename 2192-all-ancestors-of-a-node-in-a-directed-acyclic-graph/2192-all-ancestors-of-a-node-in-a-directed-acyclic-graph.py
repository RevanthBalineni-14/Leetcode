class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.res = [[] for _ in range(n)]
        self.grp = [[] for _ in range(n)]
        
        for i in edges:
            self.grp[i[0]].append(i[1])
            
        def dfs(self, par, curr, visited):
            visited[curr] = True
            for i in self.grp[curr]:
                if not visited[i]:
                    self.res[i].append(par)
                    dfs(self, par, i,visited)
                    
        for i in range(n):
            dfs(self, i, i, [False]*n)
            
        
                    
        
        for i in range(n):
            self.res[i].sort()
            
        print(self.res)
        return self.res