from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_counts = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                product_counts[product] += 1

        result = 0
        for prod, x in product_counts.items():
            if x > 1:
                result += (x*(x-1)//2)*8 

        return result