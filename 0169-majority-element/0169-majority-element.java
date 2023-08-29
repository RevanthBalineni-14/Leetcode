class Solution {
    public int majorityElement(int[] nums) {
        int maj=nums[0];
        int cnt=1;
        for(int i=1;i<nums.length;i++){
            if(maj==nums[i])
                cnt++;
            else cnt--;
            if(cnt==0){
                maj=nums[i];
                cnt=1;
            }
        }
        return maj;
    }
}