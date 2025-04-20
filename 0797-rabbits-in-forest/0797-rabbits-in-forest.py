from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        for i in answers:
            count[i+1] += 1
        res = 0
        for key in count:
            res += math.ceil(count[key]/key) * key
        return res