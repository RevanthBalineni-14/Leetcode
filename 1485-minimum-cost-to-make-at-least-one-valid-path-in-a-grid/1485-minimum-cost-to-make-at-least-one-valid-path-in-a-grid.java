class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
        int[][] dp = new int[m][n];
        for(int i=0;i<m;i++){
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        dp[0][0] = 0;

        Queue<int []> queue = new LinkedList<int[]>();
        queue.add(new int[]{0,0,0});
        while(queue.size()>0){
            int[] curr = queue.remove();
            for(int i=0; i<4; i++){
                int ni = curr[0] + dirs[i][0];
                int nj = curr[1] + dirs[i][1];
                if(0<=ni && ni<m && 0<=nj && nj<n){
                    if((i+1)==grid[curr[0]][curr[1]]){
                        if(dp[ni][nj]>curr[2]){
                            queue.add(new int[]{ni, nj, curr[2]});
                        }
                        dp[ni][nj] = Math.min(dp[ni][nj], curr[2]);
                    }else{
                        if(dp[ni][nj]>(curr[2]+1)){
                            queue.add(new int[]{ni, nj, curr[2]+1});
                        }
                        dp[ni][nj] = Math.min(dp[ni][nj], curr[2]+1);
                    }
                }
            }
        }
        return dp[m-1][n-1];
    }
}