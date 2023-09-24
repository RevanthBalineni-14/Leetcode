class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        crt=self.par[x]
        while (crt!=self.par[crt]):
            self.par[crt] = self.par[self.par[crt]]
            crt = self.par[crt]
        return crt
    
    def union(self, x1, x2):
        p1,p2=self.find(x1),self.find(x2)
        if(p1==p2):
            return False

        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=self.par[p1]
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=self.par[p2]
            self.rank[p2]+=self.rank[p1]
        
        return True
        

class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        dictionary = {}

        for i , a in enumerate(accounts):
            for e in a[1:]:
                if e in dictionary:
                    uf.union(i, dictionary[e])
                else:
                    dictionary[e] = i

        emailgrp = defaultdict(list)

        for e, i in dictionary.items():
            leader=uf.find(i)
            emailgrp[leader].append(e)
         
        res = []

        for i, e in emailgrp.items():
            res.append([accounts[i][0]]+sorted(emailgrp[i]))
        
        return res