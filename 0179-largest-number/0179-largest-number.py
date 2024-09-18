from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_numbers(x, y):
            x = str(x)
            y=str(y)
            if int(x+y)>int(y+x):
                return -1
            else:
                return 1
                
        key_func = cmp_to_key(compare_numbers)
        
        sorted_arr = sorted(nums, key = key_func)
        res = ''
        for i in sorted_arr:
            res += str(i)
            
        return str(int(res))