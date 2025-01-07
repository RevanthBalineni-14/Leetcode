import java.util.HashSet;
import java.util.Set;

class Solution {
    public List<String> stringMatching(String[] words) {
        Set <String> res = new HashSet<>();
        for(int i = 0; i<words.length; i++){
            for(int j=0; j<words.length; j++){
                if( words[i].contains(words[j])){
                    if (i!=j){
                        res.add(words[j]);
                    }
                }
            }
        }

        List<String> arr = new ArrayList<>(res);
        return arr;
    }
}