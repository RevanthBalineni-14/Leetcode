class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirs = {}
        dirs['N'] = [0, 1]
        dirs['S'] = [0, -1]
        dirs['E'] = [1, 0]
        dirs['W'] = [-1, 0]
        count = defaultdict(int)
        x, y = 0, 0
        res = 0
        originalk = k
        for i in s:
            x += dirs[i][0]
            y += dirs[i][1]
            count[i] += 1
            cres = abs(x) + abs(y)
            if(count['N']>count['S']):
                cres += min(k, count['S'])*2
                k = k - min(k, count['S'])
                if count['W']>count['E']:
                    cres += min(k, count['E'])*2
                else:
                    cres += min(k, count['W'])*2
            else:
                cres += min(k, count['N'])*2
                k = k - min(k, count['N'])
                if count['W']>count['E']:
                    cres += min(k, count['E'])*2
                else:
                    cres += min(k, count['W'])*2
            res = max(res, cres)
            k = originalk


        cres = abs(x) + abs(y)

        if(count['N']>count['S']):
            cres += min(k, count['S'])*2
            k = k - min(k, count['S'])
            if count['W']>count['E']:
                cres += min(k, count['E'])*2
            else:
                cres += min(k, count['W'])*2
        else:
            cres += min(k, count['N'])*2
            k = k - min(k, count['N'])
            if count['W']>count['E']:
                cres += min(k, count['E'])*2
            else:
                cres += min(k, count['W'])*2

        res = max(res, cres)

        return res
        
        