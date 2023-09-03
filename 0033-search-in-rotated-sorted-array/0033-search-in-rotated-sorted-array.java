class Solution {
    public int search(int[] nums, int target) {
        int pivot = pivotSearch(nums);
        int first = bSearch(nums,target,0,pivot);
        if(first == -1){
            first = bSearch(nums,target,pivot+1,nums.length-1);
        }
        return first;
    }
    private int pivotSearch(int[] nums){
        int st = 0;
        int end = nums.length-1;

        while(st<end){
            int mid = st + (end-st)/2;

            if(nums[mid] > nums[mid+1])
                return mid;
            else if(nums[mid] > nums[0])
                st = mid+1;
            else end = mid;
        }
        return nums.length-1;
    }
    private int bSearch(int[] nums,int num , int st , int end){
        while(st<=end){
            int mid = st+(end-st)/2;
            if(num > nums[mid])
                st = mid+1;
            else if(num < nums[mid])
                end = mid-1;
            else return mid;
        }
        return -1;
    }
}