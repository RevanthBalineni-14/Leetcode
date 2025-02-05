class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        dic1, dic2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
            dic1[s1[i]] += 1
            dic2[s2[i]] += 1
        
        for i in dic1:
            if dic1[i]!=dic2[i]:
                return False
        if count<=2:
            return True
        else:
            return False