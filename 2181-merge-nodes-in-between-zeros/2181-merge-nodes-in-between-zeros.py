# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        crtsum = 0
        res = None
        reshead = None
        while(head):
            if not head.val and crtsum:
                if not res:
                    res = ListNode(crtsum, None)
                    reshead = res
                else:
                    res.next = ListNode(crtsum, None)
                    res = res.next
                crtsum = 0
            else:
                crtsum += head.val
            
            head = head.next
        
        return reshead