class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        set1 = set()
        mydic = {}
        for i in s1.split():
            mydic[i] = mydic.get(i,0)+1
            
        
                
        mydic2 = {}
        set2 = set()
        
        
        for i in s2.split():
            mydic2[i] = mydic2.get(i,0)+1
            
            
        for i in mydic.keys():
            if mydic[i]==1 and i not in mydic2.keys():
                set1.add(i)
        for i in mydic2.keys():
            if mydic2[i]==1 and i not in mydic.keys():
                set2.add(i)
        return list(set1-set2) + list(set2-set1)