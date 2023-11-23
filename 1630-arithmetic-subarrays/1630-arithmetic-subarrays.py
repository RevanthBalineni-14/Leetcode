class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArthi(nums, l, r):
            maxv = float('-inf')
            minv = float('inf')
            for i in range(l,r+1):
                if maxv<nums[i]:
                    maxv=nums[i]
                if minv>nums[i]:
                    minv=nums[i]
            
            if maxv-minv==0:
                return True
            if (maxv-minv)%(r-l) != 0:
                return False

            diff = (maxv-minv)//(r-l)

            vis = [False]* (r-l+1)

            for i in range(l,r+1):
                if (nums[i]-minv)%(diff)!=0:
                    return False
                ind = (nums[i]-minv)//(diff)

                if not vis[ind]:
                    vis[ind]=True
                else:
                    return False            
            return True
        res = []
        for i in range(len(l)):
            res.append(isArthi(nums, l[i], r[i]))
        
        return res