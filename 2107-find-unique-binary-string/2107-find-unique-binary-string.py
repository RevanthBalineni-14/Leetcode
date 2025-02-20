class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        myset = set()
        n = len(nums[0])
        myset.update(nums)
        res = ""
        def traverse(cval, n):
            nonlocal myset, res
            if len(cval) == n:
                if cval not in myset:
                    res = cval
                    return True
                else:
                    return False
            for i in [0,1]:
                if traverse(cval+str(i), n):
                    return True

        traverse("", n)
        return res