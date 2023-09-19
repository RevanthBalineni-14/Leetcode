class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        maxi=0
        while left < right:
            maxi=max(maxi, min(height[right], height[left])*(right-left))
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        
        return maxi