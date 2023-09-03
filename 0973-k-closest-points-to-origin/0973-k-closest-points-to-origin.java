class Solution {
    
    public int[][] kClosest(int[][] points, int k) {
        Arrays.sort(points,(pb,pa)->pb[0]*pb[0]+pb[1]*pb[1]-pa[0]*pa[0]-pa[1]*pa[1]);
        return Arrays.copyOfRange(points,0,k);
    }
}