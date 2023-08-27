/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    boolean findNode(TreeNode root, TreeNode target,Stack<Integer> s){
        if(root==null)
            return false;
        if(root.val==target.val){
           s.push(root.val);
            return true;
        }
        if(findNode(root.left, target, s)){
            s.push(root.val);
            return true;
        }
        if(findNode(root.right, target, s)){
            s.push(root.val);
            return true;
        }
        return false;
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Stack<Integer> sp =new Stack<Integer>();
        Stack<Integer> sq=new Stack<Integer>();
        findNode( root, p, sp);
        findNode( root, q, sq);
        int common=root.val;
        if(sp.isEmpty()||sq.isEmpty())
            return new TreeNode(common);
        System.out.println(sp.peek()+" "+sq.peek());
        while(sp.peek().equals(sq.peek())){
            common=sp.peek();
            sp.pop();
            sq.pop();
            if(sp.isEmpty()||sq.isEmpty())
            return new TreeNode(common);
//            System.out.println("'"+sp.peek()+"' '"+sq.peek()+"' "+(sp.peek()==sq.peek()));
        }        
        return new TreeNode(common);
    }
}