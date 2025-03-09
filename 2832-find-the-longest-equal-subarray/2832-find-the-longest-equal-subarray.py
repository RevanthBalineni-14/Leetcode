class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        indexmap = defaultdict(list)
        for ind, i in enumerate(nums):
            indexmap[i].append(ind)
        
        res = 1
        # print(indexmap)
        for ckey in indexmap.keys():
            removed = []
            for i in range(len(indexmap[ckey])-1):
                removed.append(indexmap[ckey][i+1]-indexmap[ckey][i]-1)
            # print(removed)
            spos, clen, crem  = 0, 1, 0
            for i in removed:
                crem += i
                clen += 1
                while crem>k:
                    crem -= removed[spos]
                    spos += 1
                    clen -= 1

                res = max(res, clen)
        return res