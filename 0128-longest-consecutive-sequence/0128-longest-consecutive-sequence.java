class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> hset = new HashSet<Integer>();
        for(int i=0; i<nums.length; i++){
            hset.add(nums[i]);
        }
        int res = 0;
        for(int num: hset){
            if(!hset.contains(num-1)){
                res = Math.max(res, traverse(num, hset));
            }
        }
        return res;
    }

    public int traverse(int curr, HashSet<Integer> hset){
        int clength = 1;
        while(hset.contains(curr + 1)){
            curr++;
            clength++;
        }
        return clength;
    }
}