class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        Max = 2147483647
        y=0
        while x:
            if(y>Max//10 or (y==Max//10 and int(math.fmod(x,10))>=7)):
                return 0
            
            if(y<MIN//10 or (y==MIN//10 and int(math.fmod(x,10))<=MIN%10)):
                return 0
            
            y=int(math.fmod(x,10)) + y*10
            x=int(x/10)
        
        return y
            