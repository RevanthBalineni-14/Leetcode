class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = crt = 0
        res = 0
        for i in bank:
            tmp = 0
            for j in range(len(i)):
                if i[j]=="1":
                    tmp+=1
            if tmp>0: 
                if crt>0:
                    prev=crt
                    crt=tmp
                    res += prev*crt
                else:
                    crt = tmp
        
        return res