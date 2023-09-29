class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        tcount = {}
        window = {}
        for c in t:
            tcount[c] = 1 + tcount.get(c,0)
        l = 0

        have, need = 0, len(tcount)
        res, resl = [-1,-1], 10**6

        for r in range(len(s)):
            c = s[r]
            window[c]=window.get(c,0) + 1
            if c in t and window[c]==tcount[c]:
                have += 1

            while have == need:
                if (r-l+1)<resl:
                    res = [l,r]
                    resl = r-l+1

                window[s[l]]-=1
                if s[l] in t and window[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        
        if resl==10**6:
            return ""
        else:
            return s[res[0]:res[1]+1]