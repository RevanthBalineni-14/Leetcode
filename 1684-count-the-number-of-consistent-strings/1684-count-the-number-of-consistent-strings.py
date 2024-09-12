class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set()
        for i in allowed:
            allow.add(i)
        res = 0
        for i in range(len(words)):
            flag = True
            for j in words[i]:
                if j not in allow:
                    flag = False
            res += 1 if flag else 0
        
        return res
            