class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return None
        check = list(words[0])
        for word in words:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check