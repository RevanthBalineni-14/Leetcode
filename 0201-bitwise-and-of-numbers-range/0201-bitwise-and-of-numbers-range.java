class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        if(left==0){
            return 0;
        }
        int mf = 1;
        while(left!=right){
            left>>=1;
            right>>=1;
            mf <<= 1;
        }
        return left*mf;
    }
}