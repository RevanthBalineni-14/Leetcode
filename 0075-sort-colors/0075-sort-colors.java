class Solution {
    public void sortColors(int[] nums) {
        HashMap<Integer,Integer> h=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            System.out.println(nums[i]+" "+(h.getOrDefault(h.get(nums[i]),0)+1));
            h.put(nums[i],h.getOrDefault(nums[i],0)+1);
        }
        int count=0;
        int i,j;
        for( i=0;i<3;i++){
            if(h.containsKey(i)){
                for( j=count;j<(count+h.get(i));j++){
                    nums[j]=i;
                }
                count=j;
            }
        }
    }
}