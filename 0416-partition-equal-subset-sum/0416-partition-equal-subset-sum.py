class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 == 1:
            return False

        target = total//2

        sums = set()
        sums.add(0)

        for i in nums:
            current = set(sums)
            for j in sums:
                if(j+i==target):
                    return True

                if(j+i>target):
                    continue
                
                current.add(j+i)
            
            sums=current
        
