class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def count(dist):
            res, crt = 1, position[0]
            for i in range(1,n):
                if position[i]-crt>=dist:
                    res+=1
                    crt= position[i]
            return res
        
        l, r = 0, position[-1]-position[0]
        
        while l<r:
            mid = r- (r-l)//2
             
            if count(mid)>=m:
                l = mid 
            else:
                r = mid -1
        
        return l