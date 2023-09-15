class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> l =new ArrayList<Integer>();
        int[][] direction={{0,1},{1,0},{0,-1},{-1,0}};
        int d=0;
        int i=0,j=0;
        while(l.size()<matrix.length*matrix[0].length){
            l.add(matrix[i][j]);
            matrix[i][j]=-101;
            i=i+direction[d][0];
            j=j+direction[d][1];
            if(i<0||i>(matrix.length-1)||j<0||j>(matrix[0].length-1)||matrix[i][j]==-101){
                i=i-direction[d][0];
                j=j-direction[d][1];
                d=(d+1)%4;
                i=i+direction[d][0];
                j=j+direction[d][1];
                if(l.size()==matrix.length*matrix[0].length||matrix[i][j]==-101)
                    return l;
            }
        }
        return l;
    }
}