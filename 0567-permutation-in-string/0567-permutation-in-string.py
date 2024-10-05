from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1>n2:
            return False
        ccount = Counter(s2[0:n1])
        s1count = Counter(s1)
        for i in range(0, n2-n1+1):
            if s1count == ccount:
                return True
            # print(ccount)
            ccount[s2[i]] = ccount[s2[i]] - 1
            if ccount[s2[i]] == 0:
                del ccount[s2[i]]
            
            if n1+i<n2:
                if s2[n1+i] in ccount.keys():
                    ccount[s2[n1+i]] = ccount[s2[n1+i]] + 1
                else:
                    ccount[s2[n1+i]] = 1
        
        return False    

# "ab"
# "eidbaooo"
# "ab"
# "eidboaoo"          