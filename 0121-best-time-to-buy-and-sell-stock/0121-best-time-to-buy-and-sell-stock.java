class Solution {
    public int maxProfit(int[] prices) {
        int max=0,currentsum=0;
        int[] prefixarr=new int[prices.length];
        prefixarr[0]=0;
        for(int i=1;i<prices.length;i++){
            prefixarr[i]=prices[i]-prices[i-1];
        }
        for(int i=1;i<prices.length;i++){
            currentsum+=prefixarr[i];
            if(currentsum<0)
                currentsum=0;
            else if(currentsum>max)
                max=currentsum;
        }
        return max;
    }
}