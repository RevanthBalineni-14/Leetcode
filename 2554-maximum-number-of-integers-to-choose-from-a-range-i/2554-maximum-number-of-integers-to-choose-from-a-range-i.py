class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        csum = 0
        res = 0
        for i in range(1, n+1):
            if i not in banned and (csum+i)<=maxSum:
                res+=1
                csum += i
            else:
                if (csum+i)>maxSum:
                    return res
                
        
        return res