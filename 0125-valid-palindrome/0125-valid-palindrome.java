class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        int start=0,end=s.length()-1;
        while(start<end){
            if(!((int)s.charAt(start)>=97&&(int)s.charAt(start)<=122)&&!((int)s.charAt(start)>=48&&(int)s.charAt(start)<=57))
                start++;
            else if(!((int)s.charAt(end)>=97&&(int)s.charAt(end)<=122)&&!((int)s.charAt(end)>=48&&(int)s.charAt(end)<=57))
                end--;
            else if((int)s.charAt(start)==(int)s.charAt(end))
            {
                start++;
                end--;
            }
            else
                return false;
        }
        return true;
    }
}