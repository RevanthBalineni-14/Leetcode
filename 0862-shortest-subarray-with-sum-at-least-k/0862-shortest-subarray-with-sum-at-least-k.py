class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prearr = [0]*(n+1)
        
        for i in range(n):
            prearr[i+1] = prearr[i] + nums[i]
        
        dq = deque()
        res = float('inf')
        
        for i in range(n+1):
            while dq and prearr[i]-prearr[dq[0]]>=k:
                res = min(res, i-dq[0])
                dq.popleft()
            
            while dq and prearr[i]<=prearr[dq[-1]]:
                dq.pop()
            
            dq.append(i)
            
        return res if res!=float('inf') else -1