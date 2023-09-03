class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> solution=new ArrayList<>();
        List<Integer> temp=new ArrayList<Integer>();
        traverse(solution,temp,candidates,target,0);
        return solution;
    }
    void traverse(List<List<Integer>> solution,List<Integer> temp,int[] candidates,int remain,int start){
        if(remain<0)
            return;
        else if(remain==0)
            solution.add(new ArrayList<>(temp));
        else{
            for(int i=start;i<candidates.length;i++){
                temp.add(candidates[i]);
                traverse(solution,temp,candidates,remain-candidates[i],i);
                temp.remove(temp.size()-1);
            }
        }
    }
}