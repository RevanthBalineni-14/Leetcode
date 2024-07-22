class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = sorted(zip(names, heights), key= lambda x:x[1], reverse =True)
        return [name for name, _ in res]     