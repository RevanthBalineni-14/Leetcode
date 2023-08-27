/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    void merge(ListNode list1, ListNode list2){
        while(list1.next!=null){
            if((list1.val<list2.val&&list1.next.val>list2.val)||(list1.val==list2.val))
            {
                ListNode temp=list2.next;
                list2.next=list1.next;
                list1.next=list2;
                list2=temp;
                if(list2==null)
                    return;
            }
            list1=list1.next;
        }        
        list1.next=list2;
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode newHead=null;
        if(list1==null)
            return list2;
        else if(list2==null)
            return list1;
        else if(list1.val<=list2.val){
            newHead=list1;
            merge(list1,list2);
        }else if(list2.val<list1.val){
            newHead=list2;
            merge(list2,list1);
        }
        return newHead;
    }
}