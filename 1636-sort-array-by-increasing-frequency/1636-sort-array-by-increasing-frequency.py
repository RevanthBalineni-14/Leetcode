class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        res = sorted(nums, key= lambda x: (dic[x],-x))
        return res