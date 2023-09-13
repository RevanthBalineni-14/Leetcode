class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] isvalid=new boolean[s.length()+1];
        isvalid[0]=true;
        for(int i=1;i<=s.length();i++){
            for(int j=0;j<i;j++){
                if(isvalid[j]&&wordDict.contains(s.substring(j,i))){
                    isvalid[i]=true;
                    break;
                }
            }
        }
        return isvalid[s.length()];
    }
}