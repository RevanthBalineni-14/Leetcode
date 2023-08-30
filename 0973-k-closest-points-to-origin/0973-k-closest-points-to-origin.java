class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int []> q=new PriorityQueue<>((p1,p2)->(-p1[1]*p1[1]-p1[0]*p1[0]+p2[1]*p2[1]+p2[0]*p2[0]));
        for(int i=0;i<points.length;i++){
            q.offer(points[i]);
            if(q.size()>k)
                q.poll();
        }
        int[][] result=new int[k][2];
        while(k>0){
            k--;
            result[k]=q.poll();
        }
        return result;
    }
}