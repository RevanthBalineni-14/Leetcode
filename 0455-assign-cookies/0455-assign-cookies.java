import java.util.Arrays;
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int i=0, j=0;
        int ct = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        while(i<g.length && j<s.length){
            if(g[i]<=s[j]){
                ct++;
                i++;
                j++;
            }else{
                j++;
            }
        }
        return ct;
    }
}