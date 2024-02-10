class Solution {
    public int countSubstrings(String s) {
        if(s.length()==0){
            return 0;
        }
        int res=0;
        for(int i=0; i<s.length(); i++){
            res += counter(i, i, s);
            res += counter(i, i+1, s);
        }
        return res;
    }
    public int counter(int i, int j, String s){
        int count = 0;
        while(i>=0 && j<s.length() && s.charAt(i)==s.charAt(j)){
            count++;
            i--;
            j++;
        }
        return count;
    }
}