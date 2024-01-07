class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        mylist = [{} for _ in range(len(nums))]
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev = mylist[j].get(diff, 0)
                mylist[i][diff] = mylist[i].get(diff, 0) + prev + 1
                res += prev
        
        return res