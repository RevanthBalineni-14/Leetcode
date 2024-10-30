class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def calgcd(a,b):
            while b:
                a, b = b, a % b
            return a
        
        def findmax(i, nums):
            if i==0:
                gcd = nums[1]
            else:
                gcd = nums[0]
            
            lcm = gcd
            
            for j in range(2 if i == 0 else 1, len(nums)):
                if j == i:
                    continue
                gcd = calgcd(gcd, nums[j])  
                lcm = (nums[j] * lcm) // calgcd(nums[j], lcm)
            
            return lcm * gcd
                
        
        if len(nums) == 1:
            return nums[0]*nums[0]
        
        res = findmax(-1, nums)
        
        for i in range(len(nums)):
            res = max(res, findmax(i, nums))
            
        return res