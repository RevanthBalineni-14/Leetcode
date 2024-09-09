# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-10]*n for _ in range(m)]
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        count = 0
        i, j = 0, 0
        cdir = 0
        while count < m*n:
            if head:
                res[i][j] = head.val
                head = head.next
                
            else:
                res[i][j] = -1
                
            count +=1
            ni = i + dirs[cdir][0]
            nj = j + dirs[cdir][1]
            
            if 0 <= ni < m and 0 <= nj < n and res[ni][nj]==-10:
                i = ni
                j = nj
            else:
                cdir = (cdir+1)%4
                i = i + dirs[cdir][0]
                j = j + dirs[cdir][1]
        
        return res        