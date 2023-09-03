class Solution {
    void dfs(Stack<int[]> st,int[][] grid){
        while(!st.isEmpty()){
            int[] points=st.pop();
            int i=points[0];
            int j=points[1];
            if(i+1<grid.length&&grid[i+1][j]==1){
                grid[i+1][j]=2;
            }
            if(i-1>=0&&grid[i-1][j]==1){
                grid[i-1][j]=2;
            }
            if(j+1<grid[0].length&&grid[i][j+1]==1){
                grid[i][j+1]=2;
            }
            if(j-1>=0&&grid[i][j-1]==1){
                grid[i][j-1]=2;
            }
        }
    }
    
    public int orangesRotting(int[][] grid) {
        int count=0,flag=0,changeflag=0;
        boolean haschanged=true;
        Stack<int[]> st=new Stack<int[]>();
        if(grid==null)
            return -1;
        int[][] previousgrid=new int[grid.length][grid[0].length];
        while(haschanged){
                flag=0;changeflag=0;
                for(int i=0;i<grid.length;i++){
                    for(int j=0;j<grid[0].length;j++){
                            previousgrid[i][j]=grid[i][j];
                    }
                }

                for(int i=0;i<grid.length;i++){
                    for(int j=0;j<grid[0].length;j++){
                            if(grid[i][j]==1)
                                flag=1;
                    }
                }

                if(flag==0){
                    return count;
                }
                else{
                        for(int i=0;i<grid.length;i++){
                            for(int j=0;j<grid[0].length;j++){
                                    if(grid[i][j]==2)
                                    {
                                        st.push(new int[]{i,j});
                                    }
                            }
                        }
                }
                    count++;
                    dfs(st,grid);
                    for(int i=0;i<grid.length;i++)
                            for(int j=0;j<grid[0].length;j++)
                                if(grid[i][j]!=previousgrid[i][j])
                                {
                                    changeflag=1;
                                    break;
                                }
                    if(changeflag==0)
                        haschanged=false;
        }
        return -1;
    }
}