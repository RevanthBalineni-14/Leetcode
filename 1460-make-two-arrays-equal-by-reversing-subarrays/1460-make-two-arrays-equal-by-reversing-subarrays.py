class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if sorted(target) != sorted(arr):
            return False
        
        return True