# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        """
        slow = head
        if not head or not head.next:
            return True
        fast = head.next
        
        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        second_half = self.reverseList(slow)
        
        # Compare the first and reversed second half
        while second_half and head:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True
    
    # Helper function to reverse a linked list
    def reverseList(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev