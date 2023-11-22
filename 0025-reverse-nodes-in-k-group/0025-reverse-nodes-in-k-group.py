# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        crt = head
        ct = 0
        while ct<k and crt:
            crt=crt.next
            ct+=1
        if ct!=k:
            return head
        crt=head
        prev = None
        nxt = None
        ct = 0

        while crt and ct<k:
            nxt = crt.next
            crt.next = prev
            prev = crt
            crt = nxt
            ct += 1

        if nxt is not None:
            head.next = self.reverseKGroup(nxt, k)
        
        return prev