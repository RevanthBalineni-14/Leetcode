class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        @cache
        def traverse(ind, extra):
            if ind>=n:
                return extra
            
            min_extra = traverse(ind+1, extra)
            for i in dictionary:
                if  s[ind:].startswith(i):
                    min_extra = min(min_extra, traverse(ind+len(i), extra-len(i)))
            
            return min_extra
        
        return traverse(0, n)