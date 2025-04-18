class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prevRLE = self.countAndSay(n-1)
        currDigit = prevRLE[0]
        currCount = 1
        res = ""

        for i in range(1, len(prevRLE)):
            if(prevRLE[i]==currDigit):
                currCount += 1
            else:
                res += str(currCount) + currDigit
                currDigit = prevRLE[i]
                currCount = 1
        
        res += str(currCount) + currDigit
        return res