class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        boolean[][] pvalid = new boolean[heights.length][heights[0].length];
        boolean[][] avalid = new boolean[heights.length][heights[0].length];
        
        List<List<Integer>> res = new ArrayList<>();

        for(int i=0; i<heights.length; i++){
            for(int j=0; j<heights[0].length; j++){
                boolean[][] pvisited = new boolean[heights.length][heights[0].length];
                boolean[][] avisited = new boolean[heights.length][heights[0].length];
                canPacific(i, j, heights, pvalid, pvisited);
                canAtlantic(i, j, heights, avalid, avisited);
                if(avalid[i][j] && pvalid[i][j]){
                    Integer[] newList = {i,j};
                    res.add(Arrays.asList(newList));
                }
            }
        }

        return res;
    }

    int[][] dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
    public boolean isValid(int rows, int cols, int trow, int tcol){
        if(trow>-1 && trow<rows && tcol>-1 && tcol<cols){
            return true;
        }
        return false;
    }

    public boolean canPacific(int crow, int ccol, int[][]height, boolean[][]pvalid, boolean[][] pvisited){
        if(pvisited[crow][ccol]){
            return pvalid[crow][ccol];
        }
        if(crow==0 || ccol==0 || pvalid[crow][ccol] ){
            if(pvalid[crow][ccol]!=true){
                pvalid[crow][ccol] = true;
            }
            pvisited[crow][ccol] = true;
            return true;
        }
        pvisited[crow][ccol] = true;

        for(int i=0; i<dirs.length; i++){
            int trow = crow + dirs[i][0];
            int tcol = ccol + dirs[i][1];
            if(isValid(height.length, height[0].length, trow, tcol) && height[trow][tcol]<=height[crow][ccol]){
                pvalid[crow][ccol] = canPacific(trow, tcol, height, pvalid, pvisited);
                if(pvalid[crow][ccol]){
                    return true;
                }
            }
        }

        return pvalid[crow][ccol];
    }

    public boolean canAtlantic(int crow, int ccol, int[][]height, boolean[][]avalid, boolean[][] avisited){
        if(avisited[crow][ccol]){
            return avalid[crow][ccol];
        }
        if(crow==(height.length-1) || ccol==(height[0].length-1) || avalid[crow][ccol]){
            if(avalid[crow][ccol]!=true){
                avalid[crow][ccol] = true;
            }
            avisited[crow][ccol] = true;
            return true;
        }
        avisited[crow][ccol] = true;

        for(int i=0; i<dirs.length; i++){
            int trow = crow + dirs[i][0];
            int tcol = ccol + dirs[i][1];
            if(isValid(height.length, height[0].length, trow, tcol) && height[trow][tcol]<=height[crow][ccol]){
                avalid[crow][ccol] = canAtlantic(trow, tcol, height, avalid, avisited);
                if(avalid[crow][ccol]){
                    return true;
                }
            }
        }

        return avalid[crow][ccol];
    }
}