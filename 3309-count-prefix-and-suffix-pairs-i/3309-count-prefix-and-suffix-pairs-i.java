class Solution {
    public boolean isPrefixAndSuffix(String str1, String str2){
        if(str2.startsWith(str1) && str2.endsWith(str1)){
            return true;
        }
        else{
            return false;
        }
    }
    public int countPrefixSuffixPairs(String[] words) {
        int count = 0;
        for(int i = words.length-1; i>-1; i--){
            for(int j=0; j<i; j++){
                if (isPrefixAndSuffix(words[j], words[i])){
                    count++;
                }
            }
        }
        return count;
    }
}