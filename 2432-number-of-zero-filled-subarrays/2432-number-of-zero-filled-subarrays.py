class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        currentStreak = 0
        
        for num in nums:
            if num == 0:
                currentStreak += 1
                ans += currentStreak
            else:
                currentStreak = 0
                
        return ans