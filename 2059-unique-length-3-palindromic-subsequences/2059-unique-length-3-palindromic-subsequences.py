class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        prefdic = {}
        postdic = {}
        prefset = set()
        for i in range(len(s)):
            prefdic[i] = set(prefset) 
            prefset.add(s[i])
        
        postset = set()
        for i in range(len(s) - 1, -1, -1):
            postdic[i] = set(postset)  
            postset.add(s[i])
        
        res = 0
        cset = set()
        for i in range(1, len(s) - 1):  
            for  j in (prefdic[i].intersection(postdic[i])):
                if f"{j}{s[i]}{j}" not in cset:
                    res += 1
                    cset.add(f"{j}{s[i]}{j}")
        
        return res
