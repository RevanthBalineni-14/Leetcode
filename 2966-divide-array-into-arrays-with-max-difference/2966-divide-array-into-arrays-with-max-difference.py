class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n%3!=0:
            return False
        nums.sort()
        res = []
        count = n//3
        for i in range(count):
            crt = []
            for j in range(3):
                crt.append(nums[i*3+j])
            if (max(crt)-min(crt))>k:
                return []
            res.append(crt)
        
        return res