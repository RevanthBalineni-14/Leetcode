class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res, m = 0, {}
        for i in range(len(dominoes)):
            if dominoes[i][0]>dominoes[i][1]:
                tmp = dominoes[i][1]
                dominoes[i][1] = dominoes[i][0]
                dominoes[i][0] = tmp
            key = str(dominoes[i][0]) + "|" + str(dominoes[i][1])
            count = m.get(key, 0)
            count += 1
            m[key] = count
            res += count - 1
        return res