class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        cmin = nums[0]
        cmax = nums[0]
        
        tracker = []
        
        curr = str(bin(nums[0])).split('b')[1].count('1')
        
        for i in nums:
            newcurr = str(bin(i)).split('b')[1].count('1')
            
            if newcurr == curr:
                cmin = min(cmin, i)
                cmax = max(cmax, i)
                
            else:
                tracker.append([cmin, cmax])
                curr = newcurr
                cmin = i
                cmax = i
           
        tracker.append([cmin, cmax])
        for i in range(1, len(tracker)):
            if tracker[i-1][1] > tracker[i][0]:
                return False
            
        return True