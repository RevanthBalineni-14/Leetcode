class Solution {
    
    public int climbStairs(int n) {
        int[] arr=new int[n];
        if(n==1)
            return 1;
        if(n==2)
            return 2;
        int count=2;
        arr[0]=1;
        arr[1]=2;
        while(count<n){
            arr[count]=arr[count-1]+arr[count-2];
            count++;
        }
        return arr[count-1];
    }
}