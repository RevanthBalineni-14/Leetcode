class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        Map<Integer, int[]> hmap = new HashMap<>();
        int[] rows = new int[m];
        int[] cols = new int[n];

        Arrays.fill(rows, n);
        Arrays.fill(cols, m);

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                hmap.put(mat[i][j], new int[]{i, j});
            }
        }

        for(int i=0; i<arr.length; i++){
            int[] curr = hmap.get(arr[i]);
            int crow = curr[0], ccol = curr[1];
            rows[crow]--;
            if(rows[crow]==0){
                return i;
            }
            cols[ccol]--;
            if(cols[ccol]==0){
                return i;
            }
        }

        return -1;
    }
}