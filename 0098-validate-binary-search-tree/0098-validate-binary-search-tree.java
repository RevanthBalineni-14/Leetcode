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
    List<Integer> inorder(TreeNode root){
        List<Integer> l=new ArrayList<Integer>();
        Stack<TreeNode> st=new Stack<TreeNode>();
        while(root!=null||!st.empty()){
            while(root!=null){
                st.push(root);
                root=root.left;
            }
            root=st.pop();
            l.add(root.val);
            root=(root.right);
        }
        return l;
    }
    public boolean isValidBST(TreeNode root) {
        if(root==null)
            return true;
        List<Integer> inlist=inorder(root);
        for(int i=1;i<inlist.size();i++){
            if(inlist.get(i)<=inlist.get(i-1))
                return false;
        }
        return true;
    }
}