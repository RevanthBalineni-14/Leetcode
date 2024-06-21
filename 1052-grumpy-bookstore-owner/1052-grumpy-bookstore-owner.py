class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        gcopy = grumpy.copy()
        for i in range(0, len(customers)):
            grumpy[i] =  grumpy[i]*customers[i]
            
        for i in range(0, len(customers)):
            customers[i] =  abs(gcopy[i]-1)*customers[i]
        # print(gcopy)
        # print(grumpy)
        res = 0
        window = 0
        
        for i in range(0, len(grumpy)):
            if i<minutes:
                window += grumpy[i]
                if i==minutes-1: 
                    res = max(res, window)
            else:
                window -= grumpy[i-minutes]
                window += grumpy[i]
                res = max(res, window)
                
        
        # print(customers)
        # print(res)
        return sum(customers)+res