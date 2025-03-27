from collections import defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mp = defaultdict(int) 
        pairs = {} 
        maxi, ele = 0, 0
        n = len(nums) - 1

        for i in range(len(nums)):
            mp[nums[i]] += 1 
            
            if mp[nums[i]] > maxi:
                ele = nums[i] 
                maxi = mp[nums[i]] 
            pairs[i] = (maxi, ele)

        for i in range(len(nums) - 1):
            farr = (i + 1) // 2 
            sarr = (n - i) // 2

            freq1 = pairs[i][0] 
            freq2 = pairs[n][0] - freq1

            if freq1 > farr and freq2 > sarr and pairs[i][1] == pairs[n][1]:
                return i
        return -1 