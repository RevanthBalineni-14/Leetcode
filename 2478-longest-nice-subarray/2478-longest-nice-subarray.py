class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        window = [0]*32
        def increment(num, window):
            count = 0
            while num>0:
                window[count] += num%2
                num = num//2
                count+=1
            return
        def decrement(num, window):
            count = 0
            while num>0:
                window[count] -= num%2
                num = num//2
                count+=1
            return
        def checkAnd(window):
            for i in window:
                if i>1:
                    return False
            return True

        left, right, res = 0, 0, 1


        while right<len(nums):
            increment(nums[right], window)
            if checkAnd(window):
                res = max(res, right-left+1)
            else:
                while not checkAnd(window):
                    decrement(nums[left], window)
                    left += 1
                if (right-left)>1:
                    res = max(res, right-left+1)

            right += 1
        return res