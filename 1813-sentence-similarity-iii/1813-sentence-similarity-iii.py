class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        if len(words1)>len(words2):
            words1, words2 = words2, words1
        count = 0
        i = 0
        while i<len(words1) and words1[i] == words2[i]:
            count += 1
            i += 1
        
        i = 0
        while i<len(words1) and words1[-(i+1)] == words2[-(i+1)]:
            count += 1
            i+=1
        
        if count>=len(words1):
            return True
        
        return False