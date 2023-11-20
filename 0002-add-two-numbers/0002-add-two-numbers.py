# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        crt1 = l1
        crt2 = l2
        head = ListNode(0, None)
        headp = head
        rem =  0
        while  crt1 != None and crt2 != None:
            headp.next = ListNode((rem + crt1.val + crt2.val)%10, None)
            rem  = (rem + crt1.val + crt2.val)//10
            crt1 = crt1.next
            crt2 = crt2.next
            headp = headp.next
        
        while crt1 != None:
            headp.next = ListNode((rem + crt1.val)%10, None)
            rem = (rem + crt1.val)//10
            crt1 = crt1.next
            headp = headp.next
        
        while crt2 != None:
            headp.next = ListNode((rem + crt2.val)%10, None)
            rem = (rem + crt2.val)//10
            crt2 = crt2.next
            headp = headp.next
        
        if rem!= 0:
            headp.next = ListNode(rem, None)
        return head.next