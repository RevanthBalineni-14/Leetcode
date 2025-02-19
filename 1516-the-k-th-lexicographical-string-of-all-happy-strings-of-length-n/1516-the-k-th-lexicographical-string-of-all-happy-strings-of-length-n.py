class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def traverse(prev, maxlen, curr):
            nonlocal res
            if len(res)>=k:
                return 
            if len(curr) == maxlen:
                res.append(curr)
                return

            for i in ['a', 'b', 'c']:
                if i!=prev:
                    traverse(i, maxlen, curr+i)
        
        traverse("", n, "")
        if k>len(res):
            return ""
        else:
            return res[k-1]