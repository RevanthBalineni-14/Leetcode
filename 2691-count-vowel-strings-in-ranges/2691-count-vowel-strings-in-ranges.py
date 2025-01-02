class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def checkValid(word):
            if word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
                return 1
            return 0
        
        for i in range(len(words)):
            if i == 0:
                words[0] = checkValid(words[0])
                continue
            
            words[i] = checkValid(words[i]) + words[i-1]
        
        res = []
        for s,e in queries:
            
            if s==0 and words[0]==1:
                print(words[0], words[e])
                res.append(words[e] - words[0]+1)
                continue

            res.append(words[e] - words[max(s-1, 0)])
        
        return res