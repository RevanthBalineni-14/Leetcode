class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def checkMin(currMin):
            currCars = 0
            for i in ranks:
                currCars += int(math.sqrt((currMin)//i))
            if currCars>=cars:
                return True
            else:
                return False
        
        l, r = 0, min(ranks)*(cars**2)
        res = min(ranks)*(cars**2)
        while(l<r):
            mid = (l+r)//2
            if checkMin(mid):
                res = mid
                r = mid
            else:
                l = mid+1
        return res