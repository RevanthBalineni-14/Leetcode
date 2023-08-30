class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> l=new ArrayList<>();
        if(intervals.length<1)
            l.add(newInterval);
        
        for(int i=0;i<intervals.length;i++){
            if(newInterval[1]<intervals[0][0]){
                int[][] finalarr=new int[intervals.length+1][2];
                finalarr[0]=newInterval;
                for(int k=0;k<intervals.length;k++){
                    finalarr[k+1]=intervals[k];
                }
                return finalarr;
            }
            if((intervals[i][0]<=newInterval[0]&&newInterval[1]<=intervals[i][1])||
               (intervals[i][0]<=newInterval[1]&&newInterval[1]<=intervals[i][1])||
               (intervals[i][0]<=newInterval[0]&&newInterval[0]<=intervals[i][1])||
              (newInterval[0]<=intervals[i][0]&&intervals[i][1]<=newInterval[1])){
                newInterval[0]=Math.min(newInterval[0],intervals[i][0]);
                newInterval[1]=Math.max(newInterval[1],intervals[i][1]);
//                System.out.println(newInterval[0]+" "+newInterval[1]);
                if(l.size()>0){
                    int[] temp=l.get(l.size()-1);
                    
                    if(temp[1]<newInterval[0])
                        l.add(newInterval);
                    else{
                        l.remove(l.size()-1);
                        newInterval[0]=Math.min(newInterval[0],temp[0]);
                        newInterval[1]=Math.max(newInterval[1],temp[1]);
                        l.add(newInterval);
                    }
                }else
                    l.add(newInterval);
            }
            else if(i+1==intervals.length&&intervals[i][1]<newInterval[0]){
                l.add(intervals[i]);
                l.add(newInterval);
            }
            else if(intervals[i][1]<newInterval[0]&&intervals[i+1][0]>newInterval[1]){
                l.add(intervals[i]);
                l.add(newInterval);
            }
            else
                l.add(intervals[i]);
        }
                
        int[][] finalarr=new int[l.size()][2];
        for(int i=0;i<l.size();i++){
            finalarr[i]=l.get(i);
        }
        return finalarr;
    }
}