class Solution {
    public boolean traverse(int[][] graph, int root, HashSet<Integer> hset, boolean[] visited){
        if(hset.contains(root)){
            return true;
        }
        if(visited[root]){
            return false;
        }else{
            visited[root] = true;
        }
        boolean res = true;
        for(int i:graph[root]){
            res = res && traverse(graph, i, hset, visited);
        }
        if(res && !hset.contains(root)){
            hset.add(root);
        }
        return res;
    }

    public List<Integer> eventualSafeNodes(int[][] graph) {
        HashSet<Integer> hset = new HashSet<Integer>();
        for(int i=0; i<graph.length; i++){
            if(graph[i].length == 0){
                hset.add(i);
            }
        }

        ArrayList<Integer> res = new ArrayList<Integer>();
        boolean[] visited = new boolean[graph.length];
        for(int i=0; i<graph.length; i++){
            if(traverse(graph, i, hset, visited)){
                res.add(i);
            }
        }

        return res;
    }
}