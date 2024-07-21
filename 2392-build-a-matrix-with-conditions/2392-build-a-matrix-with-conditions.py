class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, crtp, visited, graph, res):
            if src in crtp:
                return False
            
            if src in visited:
                return True
            
            visited.add(src)
            crtp.add(src)
            
            for n in graph[src]:
                if not dfs(n, crtp, visited, graph, res):
                    return False
            
            crtp.remove(src)
            res.append(src)
            return True
    
        def tsort(edges):
            graph = defaultdict(list)
            for src, dst in edges:
                graph[src].append(dst)
            
            visited = set()
            crtp = set()
            res = []
            
            for src in range(1, k+1):
                if not dfs(src, crtp, visited, graph, res):
                    return []
            
            return res[::-1]
        
        rows = tsort(rowConditions)
        cols = tsort(colConditions)
        
        if [] in (rows, cols):
            return []
        
        vp = {
            n: [0,0] for n in range(1,k+1)
        }
        
        for ind, val in enumerate(rows):
            vp[val][0] = ind
        
        for ind, val in enumerate(cols):
            vp[val][1] = ind
        
        res = [[0 for _ in range(k)] for _ in range(k)]
        for val in range(1, k+1):
            row, col = vp[val]
            res[row][col] = val
        
        return res