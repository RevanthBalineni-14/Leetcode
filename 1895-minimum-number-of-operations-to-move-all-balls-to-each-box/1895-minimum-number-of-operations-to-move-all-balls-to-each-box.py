class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefarr = [0]*len(boxes)
        csum = 0 
        count = 0
        for i in range(len(boxes)):
            csum = csum + count
            prefarr[i] = csum
            if boxes[i]=='1':
                count += 1
        
        postarr = [0]*len(boxes)
        csum = 0 
        count = 0
        for i in range(len(boxes)-1, -1, -1):
            csum = csum+count
            postarr[i] = csum
            if boxes[i]=='1':
                count+=1

        res = [0]*len(boxes)
        for i in range(len(boxes)):
            res[i] = prefarr[i] + postarr[i]

        return res            