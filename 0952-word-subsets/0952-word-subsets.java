class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] maxFreq = new int[26];
        int[] tempFreq = new int[26];
        for(String word: words2){
            Arrays.fill(tempFreq, 0);
            for(char ch: word.toCharArray()){
                tempFreq[ch-'a']++;
            }

            for(int i=0; i<26; i++){
                maxFreq[i] = Math.max(maxFreq[i], tempFreq[i]);
            }
        }

        List<String> res = new ArrayList<>();

        for(String word: words1){
            Arrays.fill(tempFreq, 0);
            for(char ch: word.toCharArray()){
                tempFreq[ch-'a']++;
            }

            boolean flag = true;
            for(int i=0;i<26;i++){
                if(maxFreq[i]>tempFreq[i]){
                    flag = false;
                }
            }

            if(flag){
                res.add(word);
            }
        }

        return res;
    }
}