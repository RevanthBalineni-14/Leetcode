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
    List<Integer> result=new ArrayList<Integer>();
    private  boolean search(TreeNode target,TreeNode root){
        if(root==null)
            return false;
        if(root.val==target.val)
        {
            result.add(root.val);
            return true;
        }
        if(search(target, root.left))
        {
            result.add(root.val);
            return true;
        }
        else if(search(target, root.right)){
            result.add(root.val);
            return true;
        }
        return false;
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        search(p,root);
        List<Integer> lp=new ArrayList<Integer>(result);
        result.clear();
        search(q,root);
        List<Integer> lq=result;
        Collections.reverse(lp);
        Collections.reverse(lq);
        int count=0;
        while(count<lp.size()&&count<lq.size()&&lp.get(count).equals(lq.get(count)))
        {
            System.out.println(lp.get(count)+"    "+lq.get(count));
            count++;
        }
        if(count<lp.size()&&count<lq.size())
        System.out.println(lp.get(count)+"    "+lq.get(count));
        return new TreeNode(lp.get(count-1));
    }
}