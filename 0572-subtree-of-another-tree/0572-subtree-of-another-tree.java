/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean checker(TreeNode node1, TreeNode node2){
        if(node1==null && node2==null){
            return true;
        }
        if(node1==null || node2==null){
            return false;
        }
        if(node1.val!=node2.val){
            return false;
        }

        return checker(node1.left, node2.left) && checker(node1.right, node2.right);
    }

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(root==null && subRoot==null){
            return true;
        }
        if(root==null || subRoot==null){
            return false;
        }

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        while(q.peek()!=null){
            TreeNode curr = q.remove();
            if(curr.val==subRoot.val){
                if(checker(curr, subRoot)){
                    return true;
                }
            }
            if(curr.left!=null){
                q.add(curr.left);
            }
            if(curr.right!=null){
                q.add(curr.right);
            }
        }
        return false;
    }
}