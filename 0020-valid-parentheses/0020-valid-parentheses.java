import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack<String> st =new Stack<>();
        for(int i=0;i<s.length();i++){
            if(st.isEmpty()){
                st.push(""+s.charAt(i));
            }
            else{  
                if((""+s.charAt(i)).equals("(")||(""+s.charAt(i)).equals("[")||(""+s.charAt(i)).equals("{")){
                    st.push(""+s.charAt(i));
                    continue;
                }
                String head=st.pop();
                if(head.equals("(")&&(""+s.charAt(i)).equals(")"))
                    continue;
                else if(head.equals("[")&&(""+s.charAt(i)).equals("]"))
                    continue;
                else if(head.equals("{")&&(""+s.charAt(i)).equals("}"))
                    continue;
                else 
                    return false;
            }
        }
        if(st.isEmpty())
            return true;
        else 
            return false;
    }
}