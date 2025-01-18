class Tuple{
    int x;
    int y;
    Tuple(int x, int y){
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m+1][n+1];
        HashMap<String, Tuple> hmap = new HashMap<String, Tuple>();

        for(String s: strs){
            int x=0, y=0;
            for(int i=0; i<s.length(); i++){
                if(s.charAt(i)=='1'){
                    x++;
                }else{
                    y++;
                }
            }
            hmap.put(s, new Tuple(x, y));
        }

        for(String s: strs){
            for(int i=m; i>(hmap.get(s).y-1); i--){
                for(int j=n; j>(hmap.get(s).x-1); j--){
                    dp[i][j] = Math.max(dp[i][j], 1 + dp[i-hmap.get(s).y][j-hmap.get(s).x]);
                }
            }
        }

        return dp[m][n];
    }
}