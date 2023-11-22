class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        init  = [0,0]
        res = []
        crt = []
        crt.append(init)
        
        while crt:
                i = crt.pop(0)
                
                [l, r] = i
                if 0 <= l < len(nums) and 0 <= r < len(nums[l]):
                    res.append(nums[l][r])
                    if len(nums) > (l+1):
                        if [l+1,r] not in crt:
                            crt.append([l+1,r])
                    
                    if len(nums[l])>r+1:
                        if [l,r+1] not in crt:
                            crt.append([l,r+1])
        
        return res
                
        