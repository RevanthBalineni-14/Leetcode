class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] arr=new int[26];
        for(int i=0;i<26;i++)
            arr[i]=0;
        for(int i=0;i<ransomNote.length();i++)
        {
            arr[(int)ransomNote.charAt(i)-97]++;
        }
        for(int i=0;i<magazine.length();i++)
        {
            arr[(int)magazine.charAt(i)-97]--;
        }
        for(int i=0;i<26;i++){
            if(arr[i]>0)
                return false;
        }
        return true;
    }
}