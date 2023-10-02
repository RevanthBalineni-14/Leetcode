class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if colors=="A" or colors=="" or colors=="B":
            return False
        a,b = 0, 0
        for i in range(1,len(colors)-1):
            crt = colors[i]
            prev = colors[i-1]
            nxt = colors[i+1]

            if crt==prev and crt==nxt and nxt=='A':
                a+=1
            
            elif crt==prev and crt==nxt and nxt=='B':
                b+=1
        return a>b