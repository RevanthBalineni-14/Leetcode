class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sarr=new int[26];
        for(int i=0;i<=25;i++){
            sarr[i]=0;
        }
        for(int i=0;i<s.length();i++){
            sarr[(int)s.charAt(i)-97]++;
        }
        for(int i=0;i<t.length();i++){
            sarr[(int)t.charAt(i)-97]--;
        }
        for(int i=0;i<=25;i++){
            if(sarr[i]!=0)
                return false;
        }
        return true;
    }
}