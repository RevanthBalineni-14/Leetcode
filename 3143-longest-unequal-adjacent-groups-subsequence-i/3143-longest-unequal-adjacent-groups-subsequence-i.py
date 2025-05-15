class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        prev = -1
        for i in range(len(words)):
            if groups[i]!=prev:
                res.append(words[i])
                prev = groups[i]
        
        return res            