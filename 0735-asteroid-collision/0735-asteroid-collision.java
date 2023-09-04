class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> st=new Stack<>();
        for(int i=0;i<asteroids.length;i++){
            if(asteroids[i]<0&&st.isEmpty()){
                st.push(asteroids[i]);
            }else if(asteroids[i]<0&&st.peek()>0){
                int pa=st.pop();
                if(pa>Math.abs(asteroids[i]))
                    st.push(pa);
                else if(pa<Math.abs(asteroids[i])){
                    if(st.isEmpty())
                    {
                        st.push(asteroids[i]);
                    }
                    else
                        while(!st.isEmpty()){
                        pa=st.pop();
                        if(pa<0){
                            st.push(pa);
                            st.push(asteroids[i]);
                            break;
                        }
                        if(pa>0){
                            if(pa>Math.abs(asteroids[i])){
                                st.push(pa);
                                break;
                            }else if(pa==Math.abs(asteroids[i]))
                            {
                                break;
                            }else{
                                if(st.isEmpty()){
                                    st.push(asteroids[i]);
                                    break;
                                }
                            }
                        }
                    }
                }
                    
            }
            else if(asteroids[i]<0&&st.peek()<0){
                st.push(asteroids[i]);
            }
            else 
                st.push(asteroids[i]);
        }
        int[] result=new int[st.size()];
        for(int i=result.length-1;i>=0;i--){
            result[i]=st.pop();
        }
        return result;
    }
}