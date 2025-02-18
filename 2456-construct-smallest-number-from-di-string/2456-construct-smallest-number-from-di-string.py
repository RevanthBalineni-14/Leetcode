class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, temp= ["1"], []
        for i in range(len(pattern)):
            if pattern[i] == "I":
                res += temp[::-1] + [str(i+2)]
                temp = []
            else:
                temp += res.pop()
                res += [str(i+2)]

        return "".join(res)+"".join(temp[::-1])