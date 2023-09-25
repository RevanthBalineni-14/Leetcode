class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(board)
        n = len(board[0])
        def traverse(i, j, crtindex, visited):

            if (board[i][j] != word[crtindex]):
                return False

            if(crtindex==len(word)-1):
                return True

            for k, l in directions:
                if (i+k>m-1 or i+k<0 or j+l<0 or j+l>n-1):
                    continue
                if [i+k, j+l] in visited:
                    continue
                visited.append([i+k, j+l])
                if traverse(i+k, j+l, crtindex+1, visited):
                    return True
                visited.pop()
            
            return False
        
        h = {}
        for i in range(m):
            for j in range(n):
                h.clear()
                if traverse(i, j, 0, [[i,j]]):
                    return True
        
        return False