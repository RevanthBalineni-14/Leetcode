class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in details:
            crt = int(i[11:13])
            if crt>60:
                res+=1
        
        return res