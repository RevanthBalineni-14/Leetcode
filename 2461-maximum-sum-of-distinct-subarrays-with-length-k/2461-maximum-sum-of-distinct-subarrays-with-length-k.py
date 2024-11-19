class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cset = set()
        mydic = defaultdict(int)
        res = 0
        prefarr = [0]*(n+1)
        
        for i in range(n):
            prefarr[i+1] = prefarr[i] + nums[i]
            
        for i in range(k):
            if nums[i] not in cset:
                cset.add(nums[i])
            else:
                mydic[nums[i]] += 1
                 
        if len(mydic.keys()) == 0:
            res = prefarr[k]-prefarr[0]
            
        for i in range(k, n):
            if nums[i-k] in mydic.keys():
                mydic[nums[i-k]] -= 1
                if mydic[nums[i-k]] == 0:
                    del mydic[nums[i-k]]
            else:
                cset.remove(nums[i-k])
                    
            if nums[i] in cset:
                mydic[nums[i]] = mydic[nums[i]] + 1
            else:
                if len(mydic.keys())==0:
                    res = max(res, prefarr[i+1]-prefarr[i-k+1])
                cset.add(nums[i])               
            
        
        return res