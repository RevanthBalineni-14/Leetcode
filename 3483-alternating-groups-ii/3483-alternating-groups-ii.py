class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        n = len(colors)
        left, right = 0, 0
        for right in range(n+k-1):
            if right>0 and colors[right%n]==colors[(right-1)%n]:
                left = right
            
            if (right-left + 1)>=k:
                res += 1
        
        return res