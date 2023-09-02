class Solution {
    void dfs(int m,int n, char[][] grid){
        int rl=grid.length;
        int cl=grid[0].length;
        if(m<0||n<0||m>rl-1||n>cl-1||grid[m][n]!='1')
            return;
        grid[m][n]='0';
        dfs(m+1,n,grid);
        dfs(m-1,n,grid);
        dfs(m,n+1,grid);
        dfs(m,n-1,grid);
    }
    public int numIslands(char[][] grid) {
        int count=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]=='1')
                {
                    count++;
                    dfs(i,j,grid);
                }
            }
        }
        return count;
    }
    
}