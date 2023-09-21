class Solution:
    def myAtoi(self, s: str) -> int:
        Max = 2147483647
        MIN = -2147483648
        y=0
        sign=1
        s=s.strip()
        if(len(s)==0):
            return y
        print(s)
        start=0
        if(s[0]=='-'):
            sign=-1 
            start=1
        elif(s[0]=='+'):
            start=1
        print(y,sign)
        for i in range(start, len(s)):
            print(s[i])
            if (ord(s[i])>=48 and ord(s[i])<=57):
                digit = ord(s[i])-48
                if(sign ==-1 and (y>abs(MIN)//10 or y==abs(MIN)//10 and digit>=8)):
                    return MIN

                if(sign==1 and (y>Max//10 or y==Max//10 and digit>=7)):
                    return Max
                
                y = digit + y*10
            else:
                return y*sign

        print(y,sign)
        return y*sign
