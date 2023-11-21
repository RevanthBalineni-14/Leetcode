import java.util.Arrays;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int j=0,k=0;
        int res=Integer.MAX_VALUE;
        for(int i=0; i<nums.length-2;i++){
            if(i==0||i>0&&nums[i]!=nums[i-1]){
                j=i+1;
                k=nums.length-1;
                while(j<k){
                    int sum = nums[i]+nums[j]+nums[k];
                    if (Math.abs(target-res)>Math.abs(target-sum))
                          res = sum;
                    if ((nums[i]+nums[j]+nums[k])==target){
                        res=nums[i]+nums[j]+nums[k];
                        break;
                    }
                    else if(nums[i]+nums[j]+nums[k]<target)
                            j++;
                    else
                            k--;
                }
            }
        }
        return res;
    }
}

// class Solution {
//     public List<List<Integer>> threeSum(int[] nums) {
//         Arrays.sort(nums);
//         int j,k;
//         List<List<Integer>> l= new ArrayList<List<Integer>>();
//         for(int i=0;i<nums.length-2;i++){
//                 if(i==0||(i>0&&nums[i]!=nums[i-1])){
//                 int target=0-nums[i];
//                 j=i+1;
//                 k=nums.length-1;
//                 while(j<k){

//                     if(nums[j]+nums[k]==target){
//                         List<Integer> t=new ArrayList<Integer>();
//                         t.add(nums[i]);
//                         t.add(nums[j]);
//                         t.add(nums[k]);
//                         l.add(t);
//                         while(j<k&&nums[j]==nums[j+1])
//                             j++;
//                         while(j<k&&nums[k-1]==nums[k])
//                             k--;
//                         j++;k--;
//                     }
//                     else if(nums[j]+nums[k]<target)
//                         j++;
//                     else
//                         k--;
//                 }
//             }
//         }
//         return l;
//     }
// }