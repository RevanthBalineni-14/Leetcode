import java.util.*;

class Solution {
    public int findCount(ArrayList<Integer> a, ArrayList<Integer> b){
        int res = 0;
        Collections.sort(a);
        Collections.sort(b);
        int i=0, j=0;
        while(i<a.size() && j<b.size()){
            int result = a.get(i).compareTo(b.get(j));
            if(result==0){
                res++;
                i++;
                j++;
            }else if(result>0){
                j++;
            }else{
                i++;
            }
        }
        return res;
    }

    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        ArrayList<Integer> a = new ArrayList<Integer>();
        ArrayList<Integer> b = new ArrayList<Integer>();
        int[] res = new int[A.length];
        for(int i=0; i<A.length; i++){
            a.add(A[i]);
            b.add(B[i]);
            res[i] = findCount(a, b);
        }
        return res;
    }
}