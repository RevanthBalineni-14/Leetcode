# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        ct = 1
        prev = head.val
        arr = []
        while head.next.next:
            head = head.next
            ct += 1
            if (prev<head.val and head.val>head.next.val) or (prev>head.val and head.val<head.next.val):
                arr.append(ct)
            prev = head.val
        print(arr)   
        
        if len(arr)>=2:
            res[0] = arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            res[0] = min(res[0], arr[i+1]-arr[i])
            
        if len(arr)>=2:
            res[1] =  (arr[-1]-arr[0]) 
        else: 
            res[1] = -1
            
        return res