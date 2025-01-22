class Solution {
    public int hammingWeight(int n) {
        int i, res = 0;
        for(i = 0; i<32; i++){
            if(((n>>i) & 1)==1){
                res++;
            }
        }
        return res;
    }
}