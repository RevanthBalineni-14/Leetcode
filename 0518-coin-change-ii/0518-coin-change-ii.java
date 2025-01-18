class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length+1][amount+1];
        for(int i=0; i<=coins.length; i++){
            dp[i][0] = 1;
        }
        
        for(int i=1; i<=coins.length; i++){
            for(int j=0; j<=amount; j++){
                if(coins[i-1]<=j){
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]];
                }else{
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        System.out.println(dp);
        return dp[coins.length][amount];
    }
}