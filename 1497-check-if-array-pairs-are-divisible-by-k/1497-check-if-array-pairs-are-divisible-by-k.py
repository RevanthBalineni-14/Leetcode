class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = [0]*k
        
        for i in range(len(arr)):
            crt = arr[i]%k
            
            if crt<0:
                crt += k 
            
            rem[crt] +=1
        
        if rem[0]%2!=0:
            return False
        
        for i in range(1, k//2+1):
            if rem[i] != rem[k-i]:
                return False
        
        return True