class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mydic = {}
        for i in arr2:
            mydic[i] = 0 
        temp = []
        for i in arr1:
            if i in mydic.keys():
                mydic[i] += 1
            else:
                temp.append(i)
        temp.sort()
        res = []
        for i in arr2:
            for j in range(mydic[i]):
                res.append(i)
        
        res += (temp)
        return res