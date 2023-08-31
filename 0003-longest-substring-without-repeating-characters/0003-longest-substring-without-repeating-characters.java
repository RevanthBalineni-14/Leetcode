class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> h= new HashMap<>();
        int max=0,start=0;
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(h.containsKey(ch)){
                max=(i-start>max)?i-start:max;
                start=Math.max(start, h.get(ch)+1);
            }
            h.put(ch,i);
        }
        max=Math.max(max,s.length()-start);
        return max;
    }
}