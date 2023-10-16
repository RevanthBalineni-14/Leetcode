# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        m = len(lists)//2
        left = self.mergeKLists(lists[:m])
        right= self.mergeKLists(lists[m:])

        return self.merge(left,right)

    def merge(self, l, r):
        temp = ListNode(0)
        crt = temp
        while l and r:
            if (l.val<r.val):
                crt.next=l
                l=l.next
            else:
                crt.next=r
                r=r.next
            crt=crt.next
        crt.next= l or r
        return temp.next