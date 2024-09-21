class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def traverse(crt, n, res):
            if crt>n:
                return
            
            res.append(crt)
            
            traverse(crt*10, n, res)
            if crt+1 <= n and (crt+1)//10 == crt//10:
                traverse(crt+1, n, res)
            
            return
        
        res = []
        traverse(1, n, res)
        return res