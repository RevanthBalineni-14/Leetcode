class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int l=0, r=(n-1), m;
        while(l<r){
            m = (l+r)/2;
            if(nums[m]<nums[r]){
                r = m;
            }else{
                l = m+1;
            }
        }

        return nums[l];
    }
}