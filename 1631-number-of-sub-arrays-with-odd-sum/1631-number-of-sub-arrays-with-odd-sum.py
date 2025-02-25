class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9+7
        csum = 0
        odd, even = 0, 1
        res = 0
        for i in arr:
            csum += i
            if csum%2==0:
                res = (res+odd)%mod
                even += 1
            else:
                res = (res+even)%mod
                odd+=1
        return res