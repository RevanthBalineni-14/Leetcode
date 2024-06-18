class Solution:        
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit), key= lambda x: (x[0],-x[1]))
        maxp = [0]*len(profit)
        maxp[0] = jobs[0][1]
        for i, job in enumerate(jobs):
            if i==0:
                continue
            maxp[i] = max(maxp[i-1], job[1])
        
        def maxlessthan(arr, target):
            l = 0
            r = len(arr)-1
            maxless = -1
            while(l<=r):
                mid = (l+r)//2
                if arr[mid][0]>target:
                    r=mid-1
                else:
                    maxless=mid
                    l=mid+1
            return maxless
        res = 0
        for i, abil in enumerate(worker):
            maxw = maxlessthan(jobs, abil)
            if maxw!=-1:
                res+= maxp[maxw]
                
        return res