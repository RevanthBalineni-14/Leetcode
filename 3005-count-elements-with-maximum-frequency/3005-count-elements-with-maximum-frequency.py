class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mmap = {}
        for i in nums:
            mmap[i] = mmap.get(i,0) + 1
        
        maxi = 0
        for k, v in mmap.items():
            maxi = max(maxi, v)
        
        ans = 0
        for k, v in mmap.items():
            if v==maxi:
                ans=ans+v
        
        return ans