class Solution:
    def countLargestGroup(self, n: int) -> int:
        freqCounter = defaultdict(int)
        def sumOfDigits(num):
            res = 0
            while num>0:
                res += num%10
                num = num//10
            return res

        for i in range(1, n+1):
            freqCounter[sumOfDigits(i)] += 1
        res = 0
        cmax = max(freqCounter.values())
        for i in freqCounter.keys():
            if freqCounter[i] == cmax:
                res += 1
        return res