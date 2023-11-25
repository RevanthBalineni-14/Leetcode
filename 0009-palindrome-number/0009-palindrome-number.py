class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        rev = 0
        temp = x
        i = math.log(x, 10)
        i = math.floor(i)
        while temp>0:
            rev += (temp%10)*(10**i)
#            print(rev,temp)
            temp = temp//10
            i -= 1
#        print(rev)
        if(rev==x):
            return True
        return False