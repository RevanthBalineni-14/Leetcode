class MinStack {
    Stack<Integer> st;
    Stack<Integer> minStack;
    
    public MinStack() {
        st=new Stack<Integer>();
        minStack=new Stack<Integer>();
    }
    
    public void push(int val) {
        if(st.isEmpty()){
            st.push(val);
            minStack.push(val);
        }else if(val>minStack.peek()){
            int currentmin=minStack.peek();
            st.push(val);
            minStack.push(currentmin);
        }else{
            st.push(val);
            minStack.push(val);
        }
    }
    
    public void pop() {
        st.pop();
        minStack.pop();
    }
    
    public int top() {

        return st.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */