class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        hasVow, hasCon, violation = False, False, False
        if len(word)<3:
            return False
        for i in word:
            if ord(i) in {97, 101, 105, 111, 117}:
                hasVow = True
            elif 97<=ord(i)<=122 and (ord(i) not in {97, 101, 105, 111, 117}):
                hasCon = True
            elif 48<=ord(i)<=57:
                pass
            else:
                violation = True

        return hasVow & hasCon & (not violation)