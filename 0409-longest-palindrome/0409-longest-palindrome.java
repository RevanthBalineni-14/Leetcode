class Solution {
    public int longestPalindrome(String s) {
        int[] sarr=new int[26];
        int[] carr=new int[26];
        for(int i=0;i<=25;i++){
            sarr[i]=0;
            carr[i]=0;
        }
        for(int i=0;i<s.length();i++){
            if(((int)s.charAt(i))>=97)
                sarr[(int)s.charAt(i)-97]++;
            else
                carr[(int)s.charAt(i)-65]++;
        }
        int hasextra=0;
        int sum=0;
        for(int i=0;i<=25;i++){
            sum+=sarr[i]/2+carr[i]/2;
            if(sarr[i]%2==1||carr[i]%2==1)
                hasextra=1;
        }
        return sum*2+hasextra;
    }
}