class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height)-1
        sum = 0
        lmax, rmax = height[l], height[r]

        while l<r:
            if lmax <= rmax:
                l+=1
                lmax=max(lmax, height[l])
                sum+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax, height[r])
                sum+=rmax-height[r]
            
        
        return sum