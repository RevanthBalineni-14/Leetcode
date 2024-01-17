class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mydic = {}
        myset = set()
        for i in arr:
            mydic[i] = mydic.get(i, 0) + 1
        
        for k, v in mydic.items():
            if v not in myset:
                myset.add(v)
            else:
                return False
        
        return True