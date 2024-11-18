class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0]*n
        res = [0]*n
        code_extended = code * 2  

        if k > 0:
            for i in range(n):
                res[i] = sum(code_extended[i+1:i+1+k])
        else:
            for i in range(n):
                res[i] = sum(code_extended[i+n+k:i+n])
        return res
