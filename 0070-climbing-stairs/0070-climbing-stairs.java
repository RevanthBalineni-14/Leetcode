class Solution {
    
    public int climbStairs(int n) {
        if(n==1)
            return 1;
        if(n==2)
            return 2;
        int count=2;
        int one=1;
        int two=2;
        int crt=0;
        while(count<n){
            crt=one+two;
            one=two;
            two=crt;
            count++;
        }
        return crt;
    }
}