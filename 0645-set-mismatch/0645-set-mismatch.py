class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        msum = 0
        s = set()
        res = []
        for i in nums:
            if i in s:
                res.append(i)
                continue
            s.add(i)
            msum += i
        res.append((n*(n+1))//2-msum)
        return res