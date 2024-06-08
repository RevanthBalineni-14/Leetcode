class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        csum = 0
        for i, val in enumerate(nums):
            csum = (csum + val)%k
            
            if csum not in dic:
                dic[csum] = i
            else:
                if i-dic[csum]>=2:
                    return True
        
        return False