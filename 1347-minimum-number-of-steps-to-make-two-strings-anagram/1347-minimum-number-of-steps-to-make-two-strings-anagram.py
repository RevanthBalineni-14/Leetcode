class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mydic = {}
        for i in range(len(s)):
            temp = mydic.get(s[i], 0)
            mydic[s[i]] = temp + 1
        print(mydic)
        for j in range(len(t)):
            temp = mydic.get(t[j], 0)
            mydic[t[j]] = temp - 1
        print(mydic)
        res = 0
        for i in mydic:
            res += abs(mydic[i])
            
        return res//2