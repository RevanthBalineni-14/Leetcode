from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        if not s:
            return -1
        
        freqs = defaultdict(lambda: defaultdict(int))
        count = 1
        freqs[s[0]][1] = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            freqs[s[i]][count] += 1
      
        res = 0
        for char, counts in freqs.items():
            for length, freq in counts.items():
                if freq > 2:
                    res = max(res, length)
                else:
                    if length - 2 > 0:
                        res = max(res, length - 2)
                    if (length - 1) in counts and counts[length - 1] > 1:
                        res = max(res, length - 1)
        
        return res if res != 0 else -1
