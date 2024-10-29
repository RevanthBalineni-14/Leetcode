class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        prefsum = defaultdict(int)
        prefsum[0] = 1
        res = 0 
        
        for i in range(len(nums)):
            currsum += nums[i]
            res = res + prefsum[currsum-k]
            prefsum[currsum] += 1
        
        return res