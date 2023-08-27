class Solution {
    
    public int[][] floodFills(int[][] image, int sr, int sc, int color,int oc) {
        image[sr][sc]=color;
        int maxc=image[0].length;
        int maxr=image.length;
        if((sr-1)>=0)
            if(image[sr-1][sc]!=color&&image[sr-1][sc]==oc)
                floodFills(image, sr-1, sc, color, oc);
        
        if((sr+1)<maxr)
            if(image[sr+1][sc]!=color&&image[sr+1][sc]==oc)
                floodFills(image, sr+1, sc, color, oc);  
        
        if((sc-1)>=0)
            if(image[sr][sc-1]!=color&&image[sr][sc-1]==oc)
                floodFills(image, sr, sc-1, color, oc);
        
        if((sc+1)<maxc)
            if(image[sr][sc+1]!=color&&image[sr][sc+1]==oc)
                floodFills(image, sr, sc+1, color, oc);
        return image;
    }
    
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int oc=image[sr][sc];
        image[sr][sc]=color;
        return floodFills(image, sr, sc, color, oc);
    }
}