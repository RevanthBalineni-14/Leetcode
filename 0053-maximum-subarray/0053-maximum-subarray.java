class Solution {
    public int maxSubArray(int[] nums) {
        int currsum=0,maxsum=0,max=Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            if(max<nums[i])
                max=nums[i];
            currsum+=nums[i];
            if(currsum<0){
                currsum=0;
                continue;
            }
            if(maxsum<currsum)
                maxsum=currsum;
        }
        if(max>0)
        return maxsum;
        else 
            return max;
    }
}