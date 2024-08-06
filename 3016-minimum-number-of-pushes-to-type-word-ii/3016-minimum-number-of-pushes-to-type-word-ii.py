class Solution:
    def minimumPushes(self, word: str) -> int:
        fmap = Counter(word)
        print(fmap)
        mheap = []
        for i,j in fmap.items():
            mheap.append((-j, i))
        
        heapq.heapify(mheap)
        res, pos = 0, 1
        
        while mheap:
            freq, char = heapq.heappop(mheap)
            freq = -freq
            if pos < 9:
                res += freq
            elif pos < 17:
                res += 2*freq
            elif pos < 25:
                res += 3*freq
            else:
                res += 4*freq
            
            pos+=1
        
        return res