class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        carr = [0]*len(s)

        for shift in shifts:
            if shift[2] == 1:
                carr[shift[0]] += 1
                if (shift[1]+1)<len(s):
                    carr[shift[1]+1] -= 1
            else:
                carr[shift[0]] -= 1
                if (shift[1]+1)<len(s):
                    carr[shift[1]+1] += 1
        
        csum = 0
        res = []
        for i in range(len(s)):
            csum += carr[i]
            ch = chr((ord(s[i]) + csum -97)%26 + 97)
            res.append(ch)
        return ''.join(res)