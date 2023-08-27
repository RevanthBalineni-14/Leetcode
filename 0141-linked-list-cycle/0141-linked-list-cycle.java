/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head==null)
            return false;
        ListNode slow=head.next;
        if(slow==null)
            return false;
        ListNode fast=head.next.next;
        if(fast==null)
            return false;
        while(slow!=fast){
            slow=slow.next;
            if(slow==null)
                return false;
            if(fast.next==null)
                return false;
            fast=fast.next.next;
            if(fast==null)
                return false;
        }
        return true;
    }
}