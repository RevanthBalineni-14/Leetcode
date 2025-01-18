class Solution {
    public boolean canPartition(int[] nums) {
        int tsum = 0;
        for(int i=0; i<nums.length; i++){
            tsum += nums[i];
        }
        if(tsum%2==1){
            return false;
        }
        int target = (int)tsum/2;
        boolean[][] dp = new boolean[nums.length+1][target+1];

        for(int i=1;i<=nums.length; i++){
            dp[i][0] = true;
        }
        for(int j=1;j<=target; j++){
            dp[0][j] = false;
        }
        dp[0][0] = true;

        for(int i = 1; i<=nums.length; i++){
            for(int j = 1; j<=target; j++){
                dp[i][j] = dp[i-1][j];
                if(nums[i-1]<=j){
                    dp[i][j] = (dp[i][j] || dp[i-1][j-nums[i-1]]);
                }
            }
        }

        return dp[nums.length][target];
    }
}