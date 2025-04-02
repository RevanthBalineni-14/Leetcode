from collections import Counter

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hmap = Counter()
        colors = defaultdict(int)
        res = []
        for q in queries:
            if colors[q[0]]!=0:
                hmap[colors[q[0]]] -= 1
                if hmap[colors[q[0]]]==0:
                    del hmap[colors[q[0]]]

            colors[q[0]] = q[1]
            hmap[q[1]] += 1
            res.append(len(hmap.keys()))
        return res