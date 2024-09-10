# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if a==0:
                return b
            
            return gcd(b%a, a)
        
        curr = head
        
        while curr and curr.next:
            temp = curr.next
            curr.next = ListNode(gcd(curr.val, curr.next.val))
            curr.next.next = temp
            curr = curr.next.next
            
        
        return head        