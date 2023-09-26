class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        arr = [0]*26
        for i in p:
            arr[ord(i)-97]+=1
        print(arr)
        def check(array):
            for i in range(len(array)):
                if array[i]!=0:
                    return False
            
            return True
        
        j=1
        if(0+len(p)<=len(s)):
            for i in range(0,len(p)):
                arr[ord(s[i])-97]-=1
            if check(arr):
                result.append(0)
            
        while (j+len(p))<=(len(s)):
            arr[ord(s[j-1])-97]+=1
            arr[ord(s[j+len(p)-1])-97]-=1
            if check(arr):
                result.append(j)
            j+=1

        return result