class Solution {
    public int evalRPN(String[] tokens) {
        if(tokens==null)
            return 0;
        Stack<Integer> s =new Stack<Integer>();
        for(int i=0;i<tokens.length;i++){
            int val=(int)tokens[i].charAt(0);
            if((val<=57&&val>=48)||tokens[i].length()>1){
                if(tokens[i].length()>1){
                    int k=0,no=0;
                    String st=""+tokens[i].charAt(0);
                    if(st.equals("-"))
                    {
                        k=1;
                        while(k<tokens[i].length()){
                            no=no+((int)tokens[i].charAt(k)-48)*(int)Math.pow(10,tokens[i].length()-k-1);
                            k++;
                        }
                        no=-no;
                    }
                    else
                        while(k<tokens[i].length()){
                            no=no+((int)tokens[i].charAt(k)-48)*(int)Math.pow(10,tokens[i].length()-k-1);
                            k++;
                        }
                    s.push(no);
                    System.out.println(no);
                }
                else{
                    s.push(val-48);
                    System.out.println(val-48);
                }
            }
            else if(tokens[i].equals("+")){
                int a,b;
                a=s.pop();
                b=s.pop();
                s.push(a+b);
                System.out.println(a+b);
            }
            else if(tokens[i].equals("-")){
                int a,b;
                a=s.pop();
                b=s.pop();
                s.push(b-a);
                System.out.println(b-a);
            }else if(tokens[i].equals("*")){
                int a,b;
                a=s.pop();
                b=s.pop();
                s.push(b*a);
                System.out.println(b*a);
            }else{
                int a,b;
                a=s.pop();
                b=s.pop();
                s.push(b/a);
                System.out.println(b*a);
            }
        }
        return s.pop();
    }
}