import copy
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        for i in range(len(box)):
            empty_slot = len(box[0])-1
            for j in range(len(box[0])-1, -1, -1):
                if box[i][j] == '#':
                    box[i][j], box[i][empty_slot] = box[i][empty_slot], box[i][j]
                    empty_slot -= 1
                elif box[i][j] == '*':
                    empty_slot = j-1
                
            
        res = [['.']*len(box) for _ in range(len(box[0]))]
        for i in range(len(box[0])):
            for j in range(len(box)-1, -1, -1):
                res[i][len(box)-1-j] = box[j][i]
        return res