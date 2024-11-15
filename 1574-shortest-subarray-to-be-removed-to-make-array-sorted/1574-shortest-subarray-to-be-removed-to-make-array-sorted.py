class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        l, r = 0, n-1
        
        while l+1 < n and arr[l] <= arr[l+1]:
            l = l+1
        
        while r-1 > 0 and arr[r] >= arr[r-1]:
            r = r-1
        
        res = min(n-1-l, r)
        
        i = l
        j = n-1
        while i>=0 and j>=r and i < j:
            if arr[i] <= arr[j]:
                j-=1
            else:
                i-=1
            
            res = min(res, j-i)
        
        return res
                