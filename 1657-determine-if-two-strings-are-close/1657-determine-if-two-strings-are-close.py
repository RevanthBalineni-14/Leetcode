class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        s1, s2 = set(), set()
        l1, l2 = [0]*26, [0]*26
        for i in range(len(word1)):
            l1[ord(word1[i])-97] += 1
            l2[ord(word2[i])-97] += 1
            s1.add(word1[i])
            s2.add(word2[i])
        
        l1.sort()
        l2.sort()
        if s1!=s2:
            return False
        
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                return False
        
        return True