# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not ListNode:
            return []
        crt = head
        while crt:
            if crt.next:
                temp = crt.val
                crt.val = crt.next.val
                crt.next.val = temp
                crt = crt.next.next
            else:
                crt = crt.next
        
        return head