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
    int max=0;
    int finddiameter(TreeNode root){
        if(root==null)
            return 0;
        int lh=finddiameter(root.left);
        int rh=finddiameter(root.right);
        if(max<(lh+rh))
            max=lh+rh;
        return Math.max(lh,rh)+1;
    }
    public int diameterOfBinaryTree(TreeNode root) {
        finddiameter(root);
        return max;
    }
}