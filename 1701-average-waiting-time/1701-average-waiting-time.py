class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev = customers[0][0] 
        res = 0
        
        for i in range(len(customers)):
            if prev<customers[i][0]:
                prev = customers[i][0]
            res += (customers[i][1] + prev) - customers[i][0]
            prev = (customers[i][1] + prev)
        
        return res/len(customers)