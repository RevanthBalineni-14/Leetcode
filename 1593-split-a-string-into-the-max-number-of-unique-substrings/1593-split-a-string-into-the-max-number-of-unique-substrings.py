from functools import lru_cache

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.res = 1  # Store the maximum result
        
        def traverse(prevsplit, crti, crt):
            if crti == len(s):
                self.res = max(self.res, len(crt))  
                return
            current_sub = s[prevsplit:crti + 1]
            if current_sub not in crt:
                crt.append(current_sub) 
                traverse(crti + 1, crti + 1, crt) 
                crt.pop()  
            
            traverse(prevsplit, crti + 1, crt)
        
        traverse(0, 0, [])
        return self.res
