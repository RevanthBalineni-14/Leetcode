class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        
        dirs = [[0,1], [1,0], [0, -1], [-1, 0]]
        curr = 0
        maxd = 0
        obstacles=set(map(tuple,obstacles))
        for c in commands:
            if c == -1:
                curr  = (curr+1)%4
            elif c == -2:
                curr  = (curr-1)%4
            else:
                for _ in range(c):
                    nx, ny = x+dirs[curr][0], y+dirs[curr][1]
                    if (nx,ny) in obstacles:
                        break
                    x, y = nx,ny
                    maxd = max(maxd, x*x+y*y)
        return maxd