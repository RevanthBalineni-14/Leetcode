class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mydic = defaultdict(int)
        for i in nums:
            mydic[i] += 1
        res = 0
        for key in mydic.keys():
            res += mydic[key]//2
        return res==(len(nums)//2)