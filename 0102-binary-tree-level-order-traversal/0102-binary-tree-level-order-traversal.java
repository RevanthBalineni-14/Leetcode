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
    int height(TreeNode root){
        if(root==null)
            return 0;
        int lh=height(root.left);
        int rh=height(root.right);
        return Math.max(lh,rh)+1;
    }
    void traversal(List<List<Integer>> l, TreeNode root, int depth){
        if(root==null)
            return;
        l.get(depth).add(root.val);
        traversal(l,root.left,depth+1);
        traversal(l,root.right,depth+1);
    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        int h=height(root);
        List<List<Integer>> l=new ArrayList<List<Integer>>();
        for(int i=0;i<h;i++){
            l.add(new ArrayList<Integer>());
        }
        traversal(l,root,0);
        return l;
    }
}