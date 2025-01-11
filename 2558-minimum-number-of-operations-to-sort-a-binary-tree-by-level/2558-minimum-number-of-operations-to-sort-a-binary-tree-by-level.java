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
import java.util.*;

class Solution {
    public int height(TreeNode root){
        if(root == null){
            return 0;
        }
        int lh = height(root.left);
        int rh = height(root.right);
        return 1+Math.max(lh, rh);
    }
    public int minimumOperations(TreeNode root) {
        int h = height(root);
        Queue<TreeNode> q = new LinkedList<>();
        List<List<Integer>> list2D = new ArrayList<>();

        for(int i=0;i<h;i++){
            list2D.add(new ArrayList<>());
        }

        q.add(root);
        int depth = 0;

        while(!q.isEmpty()){
            int csize = q.size();
            while(csize>0){
                TreeNode croot = q.poll();
                list2D.get(depth).add(croot.val);
                if(croot.left!=null){
                    q.add(croot.left);
                }
                if(croot.right!=null){
                    q.add(croot.right);
                }
                csize--;
            }

            depth++;
        }

        int res = 0;
        
        for(List<Integer> level: list2D){
            List<Integer> sortedLevel = new ArrayList<>(level);
            Collections.sort(sortedLevel);
            HashMap<Integer, Integer> indexMap = new HashMap<Integer, Integer>();
            for(int i=0; i<sortedLevel.size(); i++){
                indexMap.put(sortedLevel.get(i), i);
            }
            
            boolean[] visited = new boolean[sortedLevel.size()];
            for(int i=0; i<sortedLevel.size(); i++){
                if(visited[i] || indexMap.get(level.get(i))==i){
                    continue;
                }
                int cycle = 0;
                int j=i;
                while(!visited[j]){
                    visited[j] = true;
                    j = indexMap.get(level.get(j));
                    cycle++;
                }
                res+= Math.max(0, cycle-1);
            }
        }

        return res;
    }
}