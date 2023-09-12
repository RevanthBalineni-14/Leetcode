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
    HashMap<Integer,Integer> h=new HashMap<Integer,Integer>();

    void dfs(TreeNode root,int depth){
        if(root==null)
            return;
        if(h.containsKey(depth)){
            dfs(root.right,depth+1);
            dfs(root.left,depth+1);
        }
        else{
            h.put(depth,root.val);
            dfs(root.right,depth+1);
            dfs(root.left,depth+1);
        }
    }
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> l = new ArrayList<Integer>();
        dfs(root,0);
        int i=0;
        while(true){
            if(h.containsKey(i))
                l.add(h.get(i));
            else break;
            i++;
        }
        return l;
    }
}