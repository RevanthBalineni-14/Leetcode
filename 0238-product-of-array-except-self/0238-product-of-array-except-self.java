class Solution {
    public int[] productExceptSelf(int[] nums) {
        if(nums==null)
            return null;
        if(nums.length==1)
            return nums;
        int product=1;
        int[] pproducts=new int[nums.length];
        int[] bproducts=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            pproducts[i]=product;
            product*=nums[i];
        }
        product=1;
        for(int i=nums.length-1;i>=0;i--){
            bproducts[i]=product;
            product*=nums[i];            
        }
        int[] products=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            System.out.println(pproducts[i]+" "+bproducts[i]);
            products[i]=pproducts[i]*bproducts[i];
        }
        return products;
    }
}