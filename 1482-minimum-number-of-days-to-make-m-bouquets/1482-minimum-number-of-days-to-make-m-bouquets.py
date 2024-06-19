class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        left = 1
        right = max(bloomDay)
        
        while left<right:
            
            flow = 0
            boquet = 0
            mid = (left + right)//2
            for i in bloomDay:
                if i>mid:
                    flow = 0
                else:
                    flow += 1
                 
                if flow>=k:
                    flow=0
                    boquet +=1
                    if boquet == m:
                        break
            # print(mid, flow, boquet)  
            if boquet == m:
                right = mid

            else:
                left = mid+1
                    
        return left
                