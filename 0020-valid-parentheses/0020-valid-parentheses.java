import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack<String> st =new Stack<>();
        for(int i=0;i<s.length();i++){
            
                if((s.charAt(i)+"").equals("(")){
                    st.push(")");
                    continue;
                }
                else if((s.charAt(i)+"").equals("[")){
                    st.push("]");
                    continue;
                }
                else if((s.charAt(i)+"").equals("{")){
                    st.push("}");
                    continue;
                }
                else if(st.isEmpty())
                    return false;
                else if(!(s.charAt(i)+"").equals(st.pop()))
                    return false;
        }
        if(st.isEmpty())
            return true;
        else 
            return false;
    }
}