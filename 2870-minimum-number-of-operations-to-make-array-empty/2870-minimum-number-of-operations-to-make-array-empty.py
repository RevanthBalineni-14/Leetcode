class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mydic = {}
        res = 0
        for i in nums:
            mydic[i] = mydic.get(i,0) + 1
        
        for i in mydic.keys():
            if mydic[i]==1:
                return -1
            
            res += mydic[i]//3
            if mydic[i]%3 > 0:
                res += 1
        return res