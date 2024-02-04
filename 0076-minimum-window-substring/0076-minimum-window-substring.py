class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""
        
        tvals = {}
        for i in t:
            tvals[i] = 1 + tvals.get(i,0)
        have, need = 0, len(tvals)
        res, resl = [], 10**6
        window = {}
        l = 0
        for i in range(len(s)):
            # print(have, need, i)
            window[s[i]]  = 1 + window.get(s[i], 0) 
            if s[i] in t and window[s[i]]==tvals[s[i]]:
                have += 1
                
            while have==need:
                if resl>(i-l+1):
                    res = [l,i]
                    resl = i-l+1
                window[s[l]] -= 1
                if s[l] in t and window[s[l]]<tvals[s[l]]:
                    have -= 1
                l += 1
        if resl == 10**6:
            return ""
        else:
            return s[res[0]:res[1]+1]