class Solution:
    def makeFancyString(self, s: str) -> str:
        pc, cc, res = None, 0, ""
        for i in s:
            if pc == None or i!=pc:
                pc = i
                cc = 1
                res += i
            else:
                if cc>=2:
                    continue
                else:
                    cc+=1
                    res+=i

        return res