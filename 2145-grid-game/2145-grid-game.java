class Solution {
    public long gridGame(int[][] grid) {
        long[] topPrefix = new long[grid[0].length+1];
        long[] bottomPrefix = new long[grid[0].length+1];
        for(int i=1;i<=grid[0].length;i++){
            topPrefix[i] = topPrefix[i-1] + grid[0][i-1];
            bottomPrefix[i] = bottomPrefix[i-1] + grid[1][i-1];
        }
        int n = grid[0].length;
        long res = Long.MAX_VALUE, cscore = 0;
        for(int i=0; i<n; i++){
            cscore = Math.max(topPrefix[n]-topPrefix[i+1], bottomPrefix[i]);
            res = Math.min(cscore, res);
        }
        return res;
    }
}