from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        alist = defaultdict(set)
        for a, b in prerequisites:
            alist[b].add(a)

        dlist = {}
        def dfs(ind):
            if ind in dlist:
                return dlist[ind]

            crt = set()
            for i in alist[ind]:
                crt.add(i)
                crt.update(dfs(i))
            
            dlist[ind] = crt
            return dlist[ind]

        res = []
        for a, b in queries:
            if a in dfs(b):
                res.append(True)
            else:
                res.append(False)
        
        return res